from functools import cached_property

from package_utils.context import Context as Context_

from ..models import Config, Options


class Context(Context_[Options, Config, None]):
    @cached_property
    def app_name(self) -> str:
        return self.config.app_name or f"{self.options.name}.server:app"

    @cached_property
    def hostname(self) -> str:
        return self.config.hostname or f"https://{self.options.name}.com"

    @cached_property
    def session_name(self) -> str:
        return context.config.session_name or f"{self.options.name}-backend"

    @cached_property
    def frontend_repository(self) -> str:
        repository = context.config.frontend_repository
        return repository or f"quintenroets/{self.options.name}-frontend"

    @cached_property
    def backend_command(self) -> str:
        debug_option = "--debug" if context.options.debug else "--no-debug"
        command_parts = "start-backend", "--name", context.options.name, debug_option
        return " ".join(command_parts)


context = Context(Options, Config)
