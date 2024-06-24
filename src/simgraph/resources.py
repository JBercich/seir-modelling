#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import operator
from enum import Enum, unique
from abc import ABC, abstractmethod
from uuid import uuid4, UUID
from typing import Any, List, Dict, Callable

from simgraph.exceptions import InvalidEntityTypeException


@unique
class SupportedOperations(Enum):
    __add__: Callable = operator.add
    __sub__: Callable = operator.sub
    __mul__: Callable = operator.mul
    __truediv__: Callable = operator.truediv
    __floordiv__: Callable = operator.floordiv
    __mod__: Callable = operator.mod
    __pow__: Callable = operator.pow
    __and__: Callable = operator.and_
    __rshift__: Callable = operator.rshift
    __lshift__: Callable = operator.lshift
    __or__: Callable = operator.or_
    __xor__: Callable = operator.xor
    __lt__: Callable = operator.lt
    __gt__: Callable = operator.gt
    __le__: Callable = operator.le
    __ge__: Callable = operator.ge
    __eq__: Callable = operator.eq
    __ne__: Callable = operator.ne


class Resource(ABC):
    def __init__(self, value: Any, name: str = ""):
        self.uuid: UUID = uuid4()
        self.name: str = name
        self.type: type = type(value)
        self.value: Any = value

    def __hash__(self) -> int:
        return hash(self.uuid)

    def __str__(self) -> str:
        return str(self.uuid)

    def __op__(self, obj: Any, op: Callable) -> Any:
        return op(self.value, obj.value if issubclass(type(obj), Resource) else obj)

    def __add__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__add__)

    def __sub__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__sub__)

    def __mul__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__mul__)

    def __truediv__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__truediv__)

    def __floordiv__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__floordiv__)

    def __mod__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__mod__)

    def __pow__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__pow__)

    def __and__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__and__)

    def __rshift__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__rshift__)

    def __lshift__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__lshift__)

    def __or__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__or__)

    def __xor__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__xor__)

    def __lt__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__lt__)

    def __gt__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__gt__)

    def __le__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__le__)

    def __ge__(self, obj: Any) -> Any:
        return self.__op__(obj, SupportedOperations.__ge__)

    def __eq__(self, obj: Any) -> bool:
        return self.__op__(obj, SupportedOperations.__eq__)

    def __ne__(self, obj: Any) -> bool:
        return self.__op__(obj, SupportedOperations.__ne__)


class Constant(Resource):
    pass


class Entity(Resource):
    def __init__(self, value: Any, name: str = ""):
        super().__init__(value, name)
        self.history: List[Any] = [self.value]
        self.depends: Dict[str, Entity] = {}

    def __step__(self, *args, **kwargs) -> None:
        self.value = self.update(**self.depends)
        if not isinstance(self.value, (self.type, type(None))):
            raise InvalidEntityTypeException(self.type, type(self.value))
        self.history.append(self.value)

    def add_dependencies(self, **dependencies) -> None:
        for k, v in dependencies.items():
            self.depends[k] = v

    @abstractmethod
    def update(self, *, _) -> Any:
        pass
