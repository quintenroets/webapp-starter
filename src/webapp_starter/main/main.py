from collections.abc import Iterator

import cli

from webapp_starter.context import context

from .frontend import Frontend


def main() -> None:
    start_backend()
    open_frontend()


def open_frontend() -> None:
    Frontend.check_content()
    if not context.options.headless:
        cli.urlopen(context.hostname)


def start_backend() -> None:
    commands = generate_commands()
    cli.run_commands(*commands, check=False)


def generate_commands() -> Iterator[str]:
    if context.options.restart:
        yield f"tmux kill-session -t {context.session_name}"

    yield f"tmux new-session -s {context.session_name} -d {context.backend_command}"
