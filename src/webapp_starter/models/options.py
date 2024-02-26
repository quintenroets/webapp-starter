from dataclasses import dataclass

from .path import Path


@dataclass
class Options:
    name: str = ""
    config_path: Path | None = None
    headless: bool = False
    debug: bool = False
    restart: bool = False
    update_frontend: bool = False
    backend: bool = False

    def __post_init__(self) -> None:
        if self.config_path is None:
            self.config_path = Path.assets / self.name / "config" / "config.yaml"
