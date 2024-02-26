import importlib
import typing

import uvicorn

from ..context import context
from ..models import Path


def main() -> None:
    if context.options.debug:  # pragma: nocover
        webapp_module = importlib.import_module(context.options.name)
        path_str = typing.cast(str, webapp_module.__file__)
        webapp_source_root = Path(path_str).parent
        reload_dirs = str(webapp_source_root)
    else:
        reload_dirs = None

    log_level = "info" if context.options.debug else "warning"
    uvicorn.run(
        context.app_name,
        port=context.config.backend_port,
        reload_dirs=reload_dirs,
        reload=context.options.debug,
        log_level=log_level,
    )
