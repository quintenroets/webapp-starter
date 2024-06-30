from collections.abc import Iterator
from unittest.mock import MagicMock, patch

import cli
import pytest
from webapp_starter.context import Context
from webapp_starter.main.main import Frontend, main


@pytest.fixture()
def frontend_opening_context(test_context: Context) -> Iterator[Context]:
    test_context.options.headless = False
    yield test_context
    test_context.options.headless = True
    test_content_path = Frontend().content_path
    cli.run("sudo rm -r", test_content_path)


@patch("webapp_starter.main.main.open_frontend")
def test_backend_start(open_frontend: MagicMock, test_context: Context) -> None:
    main()
    main()
    test_context.options.restart = True
    main()
    cli.run("tmux kill-session -t", test_context.session_name)
    open_frontend.assert_called()


@patch("cli.open_urls")
@patch("webapp_starter.main.main.start_backend")
@pytest.mark.usefixtures("frontend_opening_context")
def test_frontend_opening(open_url: MagicMock, start_backend: MagicMock) -> None:
    main()
    open_url.assert_called_once()
    start_backend.assert_called_once()


@pytest.mark.usefixtures("frontend_opening_context")
def test_frontend_update_with_existing_path() -> None:
    frontend = Frontend()
    frontend.create_content_path()
    path = frontend.content_path / "index.html"
    path.touch(mtime=0.0)
    frontend.update_content()
