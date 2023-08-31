#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import operator
from typing import Any, Callable

from simpyl.system.resources import Resource


class DataField(Resource):
    def __init__(self, value: Any, name: str):
        self._value: Any = value
        self._type: type = type(value)
        self._name: str = name

    def __eq__(self, other):
        if self.get_name() == other.get_name():
            return self.get_value() == other.get_value()
        return False

    def __lt__(self, other):
        return self.operation(other, operator.lt)

    def __add__(self, other):
        return self.operation(other, operator.add)

    def __sub__(self, other):
        return self.operation(other, operator.sub)

    def __mul__(self, other):
        return self.operation(other, operator.mul)

    def __div__(self, other):
        return self.operation(other, operator.div)

    def operation(self, other: Any, operation: Callable):
        if isinstance(other, self.__class__):
            return operation(self.get_value(), other.get_value())
        return operation(self.get_value(), other)

    def get_value(self) -> Any:
        return self._value

    def get_name(self) -> str:
        return self._name
