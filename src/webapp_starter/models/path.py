import typing
from typing import TypeVar

import superpathlib
from simple_classproperty import classproperty

T = TypeVar("T", bound="Path")


class Path(superpathlib.Path):
    @classmethod
    @classproperty
    def source_root(cls: type[T]) -> T:
        return cls(__file__).parent.parent

    @classmethod
    @classproperty
    def assets(cls: type[T]) -> T:
        path = cls.script_assets / cls.source_root.name
        return typing.cast(T, path)
