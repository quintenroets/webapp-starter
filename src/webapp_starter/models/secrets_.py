import os
from dataclasses import dataclass, field


@dataclass
class Secrets:
    github_token: str
