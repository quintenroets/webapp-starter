from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import dacite
from package_utils.dataclasses.mixins import SerializationMixin

from ..context import context


@dataclass
class FrontendRelease(SerializationMixin):
    updated_at: str
    id: int

    @classmethod
    def fetch(cls) -> FrontendRelease:
        frontend_info = context.client.fetch_json("latest")["assets"][0]
        config = dacite.Config(strict=False)
        return cls.from_dict(frontend_info, config=config)

    @property
    def mtime(self) -> float:
        format_str = "%Y-%m-%dT%H:%M:%SZ"
        return datetime.strptime(self.updated_at, format_str).timestamp()

    @property
    def fetched_content(self) -> bytes:
        return context.client.fetch_content(f"assets/{self.id}")
