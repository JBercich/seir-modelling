#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import operator
from enum import Enum, unique
from abc import ABC, abstractmethod
from uuid import uuid4, UUID
from typing import Any, List, Dict

from simgraph.exceptions import (
    UpdateTypeException,
    DuplicateDependencyException,
    InvalidDependencyException,
)


@unique
class SupportedOperations(Enum):
    __add__ = operator.add
    __sub__ = operator.sub
    __mul__ = operator.mul
    __div__ = operator.truediv


print(SupportedOperations.__add__)


_NUM_CONSTANT: int = 0
_NUM_ENTITIES: int = 0


def reset_constant_counter():
    global _NUM_CONSTANT
    _NUM_CONSTANT = 0


def reset_entity_counter():
    global _NUM_ENTITIES
    _NUM_ENTITIES = 0


class Resource(ABC):
    def __init__(self, value: Any, name: str = ""):
        self.uuid: UUID = uuid4()
        self.name: str = name
        self.type: type = type(value)
        self.value: Any = value
        self.__add__ = lambda x: self.value + x.value

    def __hash__(self) -> int:
        return hash(self.uuid)

    def __eq__(self, value: object) -> bool:
        if issubclass(type(value), Resource):
            return self.value == value.value
        return self.value == value

    def __lt__(self, value: object) -> bool:
        if issubclass(type(value), Resource):
            return self.value < value.value
        return self.value < value

    def __gt__(self, value: object) -> bool:
        if issubclass(type(value), Resource):
            return self.value > value.value
        return self.value > value

    def __le__(self, value: object) -> bool:
        if issubclass(type(value), Resource):
            return self.value <= value.value
        return self.value <= value

    def __ge__(self, value: object) -> bool:
        if issubclass(type(value), Resource):
            return self.value >= value.value
        return self.value >= value

    def __ne__(self, value: object) -> bool:
        if issubclass(type(value), Resource):
            return self.value != value.value
        return self.value != value

    # Add in operations


class Constant:
    def __init__(self, value: Any, name: str = None):
        global _NUM_CONSTANT
        self._uuid: UUID = uuid4()
        self._type: type = type(value)
        self._name: str = name if name else f"{self.__class__.__name__}:{_NUM_CONSTANT}"
        self._value: Any = value
        _NUM_CONSTANT += 1

    def __hash__(self) -> int:
        return hash(self._uuid)

    def __add__(self, other):
        return self._value + other._value


class Entity(ABC):
    def __init__(self, value: Any, name: str = None):
        global _NUM_ENTITIES
        self._uuid: UUID = uuid4()
        self._type: type = type(value)
        self._hist: List[Any] = [value]
        self._name: str = name if name else f"{self.__class__.__name__}:{_NUM_ENTITIES}"
        self._dependencies: Dict[str, Entity] = {}
        self.value: Any = value
        _NUM_ENTITIES += 1

    def __hash__(self) -> int:
        return hash(self._uuid)

    def _step(self, *args, **kwargs):
        self.value = self.update(**self._dependencies)
        if self.value is not None and not isinstance(self.value, self._type):
            raise UpdateTypeException(self._type, type(self.value))
        self._hist.append(self.value)

    def register_dependencies(self, **dependencies):
        for name, entity in dependencies.items():
            if name in self._dependencies.keys():
                raise DuplicateDependencyException(name)
            if not (isinstance(entity, Constant) or issubclass(type(entity), Entity)):
                raise InvalidDependencyException(name, entity)
            self._dependencies[name] = entity

    @abstractmethod
    def update(self, *, _) -> Any:
        pass


class Test(Entity):
    def update(self, var_a):
        return 0


entity = Test(value=12)
reset_entity_counter()
entity1 = Test(value=12)
entity.register_dependencies(var_a=entity1)
entity1.register_dependencies(var_a=entity)
# print(entity == entity1)
# print(entity == entity)
# entity._step()

print(Constant(1) + Constant(2))
