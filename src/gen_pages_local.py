import shutil
from pathlib import Path
import subsurfaceio

# 1. Define your path structures explicitly
# Source package directory (where the code lives)
package_dir = Path(subsurfaceio.__file__).resolve().parent
src_parent = package_dir.parent

# Target output directory inside the physical Zensical documentation root
script_dir = Path(__file__).resolve().parent
docs_dir = script_dir.parent / "docs"
reference_dir = docs_dir / "reference"

if reference_dir.exists():
    print(f"Cleaning stale reference files from: {reference_dir}")
    shutil.rmtree(reference_dir)

print(f"Generating API reference files in: {reference_dir}")

# 2. Scrapes files and dynamically generates reference pages
for path in sorted(package_dir.rglob("*.py")):
    # Ignore internal setup files or private modules
    if path.name.startswith("_") and path.name != "__init__.py":
        continue

    # Get path relative to the parent directory to keep the root package name
    module_path = path.relative_to(src_parent).with_suffix("")
    doc_path = path.relative_to(src_parent).with_suffix(".md")
    full_doc_path = reference_dir / doc_path

    parts = tuple(module_path.parts)

    # Handle __init__.py files cleanly by naming them index.md
    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
        if not parts:
            continue

    # 3. Ensure the physical output subdirectories exist
    full_doc_path.parent.mkdir(parents=True, exist_ok=True)

    # 4. Dynamically inject the mkdocstrings identifier string into the file
    ident = ".".join(parts)
    with open(full_doc_path, "w", encoding="utf-8") as fd:
        fd.write(f"::: {ident}\n")

    print(f" Created reference stub: {full_doc_path}")

print("Reference page generation complete.")
