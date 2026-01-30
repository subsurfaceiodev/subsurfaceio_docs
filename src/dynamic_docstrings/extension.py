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
        print(f'hello! {func.parent}')
        if self.object_paths and func.parent.path not in self.object_paths:
            return  # Skip objects that were not selected.

        # Import object to get its evaluated docstring.
        try:
            runtime_obj = griffe.dynamic_import(func.path)
            docstring = runtime_obj.__doc__
        except ImportError:
            logger.debug(f"Could not get dynamic docstring for {func.path}")
            return
        except AttributeError:
            logger.debug(f"Object {func.path} does not have a __doc__ attribute")
            return

        if not func.name.startswith('_'):
            docstring = docstrings[func.parent.path.split('.')[-1]][func.name]
            func.docstring = griffe.Docstring(
                docstring,
                parent=func,
                parser=loader.docstring_parser,
                parser_options=loader.docstring_options,
            )
