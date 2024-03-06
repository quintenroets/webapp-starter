import io
import os
import urllib.parse
import zipfile
from dataclasses import dataclass, field

import cli
from superpathlib import Path

from ..context import context
from .frontend_release import FrontendRelease


def load_dist_path() -> Path:
    domain_name = urllib.parse.urlparse(context.hostname).netloc
    return Path("/") / "var" / "www" / domain_name


@dataclass
class Frontend:
    content_path: Path = field(default_factory=load_dist_path)

    @classmethod
    def check_content(cls) -> None:
        frontend = Frontend()
        if context.options.update_frontend or frontend.content_path.is_empty():
            frontend.update_content()

    def update_content(self) -> None:
        frontend_release = FrontendRelease.fetch()
        if self.content_path.is_empty():
            mtime = 0.0
        else:
            files = self.content_path.iterdir()
            mtime = next(iter(files)).mtime
        if mtime < frontend_release.mtime:
            self.download_content(frontend_release)

    def download_content(self, frontend_release: FrontendRelease) -> None:
        if not self.content_path.exists():
            self.create_content_path()
        self.save_content(frontend_release.fetched_content)
        self.content_path.mtime = frontend_release.mtime

    def save_content(self, content: bytes) -> None:
        content_io = io.BytesIO(content)
        zip_file = zipfile.ZipFile(content_io)
        with zip_file:
            zip_file.extractall(self.content_path)

    def create_content_path(self) -> None:
        try:
            username = os.getlogin()
        except OSError:  # pragma: nocover (on GitHub action)
            username = "runner"  # pragma: nocover
        cli.run("mkdir", self.content_path, root=True)
        cli.run(f"chown -R {username}:{username}", self.content_path, root=True)
