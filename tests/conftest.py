import pytest
from webapp_starter.context import Context
from webapp_starter.context import context as context_


@pytest.fixture(scope="session")
def context() -> Context:
    return context_


@pytest.fixture(scope="session")
def test_context(context: Context) -> Context:
    context.options.name = "test"
    context.config.backend_port += 7
    context.config.frontend_repository = "quintenroets/music-frontend"
    context.options.headless = True
    return context
