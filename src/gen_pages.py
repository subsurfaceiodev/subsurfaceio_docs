from pathlib import Path
import mkdocs_gen_files
import subsurfaceio

nav = mkdocs_gen_files.Nav()

# Find the root package directory and its parent directory
package_dir = Path(subsurfaceio.__file__).resolve().parent
src_parent = package_dir.parent

# Scrapes files and dynamically generates reference pages
for path in sorted(package_dir.rglob("*.py")):
    # Ignore internal setup files or private modules if necessary
    if path.name.startswith("_") and path.name != "__init__.py":
        continue

    # Get path relative to the parent directory to keep the root package name
    module_path = path.relative_to(src_parent).with_suffix("")
    doc_path = path.relative_to(src_parent).with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = tuple(module_path.parts)

    # Handle __init__.py files cleanly in navigation
    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
        if not parts:
            continue

    # Add the file to the virtual navigation object
    nav[parts] = doc_path.as_posix()

    # Dynamically inject the mkdocstrings identifier string
    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        ident = ".".join(parts)
        fd.write(f"::: {ident}\n")

    # Set the 'Edit on GitHub' button to point directly to the source code
    mkdocs_gen_files.set_edit_path(full_doc_path, path)
