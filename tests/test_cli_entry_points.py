from unittest.mock import MagicMock, patch

import pytest
from package_dev_utils.tests.args import cli_args
from webapp_starter.cli import backend, webapp


@cli_args("--name", "test")
@patch("cli.run_commands")
@patch("cli.open_urls")
@pytest.mark.usefixtures("test_context")
def test_webapp_entry_point(run_commands: MagicMock, open_urls: MagicMock) -> None:
    webapp.entry_point()
    run_commands.assert_called_once()
    open_urls.assert_called_once()


@cli_args("--name", "test")
@patch("uvicorn.run")
@pytest.mark.usefixtures("test_context")
def test_backend_entry_point(uvicorn_run: MagicMock) -> None:
    backend.entry_point()
    uvicorn_run.assert_called_once()
