from dataclasses import dataclass


@dataclass
class Config:
    app_name: str | None = None
    hostname: str | None = None
    frontend_repository: str | None = None
    backend_port: int = 13000
    session_name: str | None = None
