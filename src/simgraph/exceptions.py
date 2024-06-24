#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import Any


class GraphException(Exception):
    pass


class EntityException(GraphException):
    pass


class UpdateTypeException(EntityException):
    def __init__(self, expected: type, returned: type):
        self.expected: type = expected
        self.returned: type = returned

    def __str__(self) -> str:
        return f"Received type {self.returned} but expected type {self.expected}"


class DuplicateDependencyException(EntityException):
    def __init__(self, name: str):
        self.name: str = name

    def __str__(self) -> str:
        return f"Variable already registered dependency: '{self.name}'"


class InvalidDependencyException(EntityException):
    def __init__(self, name: str, dependency: Any):
        self.name: str = name
        self.dependency: Any = dependency

    def __str__(self) -> str:
        return f"Cannot register invalid dependency: '{self.name}'"
