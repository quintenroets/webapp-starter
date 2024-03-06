from __future__ import annotations

import typing
from dataclasses import dataclass
from typing import Any

import requests


@dataclass
class Client:
    repository: str
    github_token: str

    def __post_init__(self) -> None:
        self.base_url: str = f"https://api.github.com/repos/{self.repository}/releases/"
        self.session = requests.Session()
        authorization = f"bearer {self.github_token}"
        self.session.headers = {
            "Authorization": authorization,
            "Accept": "application/json",
        }

    def fetch_json(self, url: str) -> dict[str, Any]:
        headers = {"Accept": "application/json"}
        result = self.fetch(url, headers=headers).json()
        return typing.cast(dict[str, Any], result)

    def fetch_content(self, url: str) -> bytes:
        headers = {"Accept": "application/octet-stream"}
        return self.fetch(url, headers=headers).content

    def fetch(
        self, url: str, headers: dict[str, str] | None = None
    ) -> requests.Response:
        full_url = self.base_url + url
        return self.session.get(full_url, headers=headers)
