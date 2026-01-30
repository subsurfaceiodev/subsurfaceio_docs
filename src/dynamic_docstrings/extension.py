import griffe
from dynamic_docstrings.function_docstrings import docstrings

logger = griffe.get_logger(__name__)


class DynamicDocstrings(griffe.Extension):
    def __init__(self, object_paths: list[str] | None = None) -> None:
        self.object_paths = object_paths

    def on_function(
            self,
            func: griffe.Function,
            loader: griffe.GriffeLoader,
            **kwargs,
    ) -> None:
        if self.object_paths and func.parent.path not in self.object_paths:
            return  # Skip objects that were not selected.

        if not func.name.startswith('_'):
            return

        try:
            module_key = func.parent.path.split('.')[-1]
            docstring = docstrings[module_key][func.name]
        except KeyError:
            return

        func.docstring = griffe.Docstring(
            docstring,
            parent=func,
            parser=loader.docstring_parser,
            parser_options=loader.docstring_options,
        )
