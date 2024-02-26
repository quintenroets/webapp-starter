from unittest.mock import MagicMock, patch

from package_dev_utils.tests.args import cli_args
from webapp_starter.cli import backend, webapp
from webapp_starter.context import Context


@cli_args("--name", "test")
@patch("cli.run_commands")
@patch("cli.urlopen")
def test_webapp_entry_point(_: MagicMock, __: MagicMock, test_context: Context) -> None:
    webapp.entry_point()


@cli_args("--name", "test")
@patch("uvicorn.run")
def test_backend_entry_point(_: MagicMock, test_context: Context) -> None:
    backend.entry_point()
