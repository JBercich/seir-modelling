#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import operator
from typing import Any

from simpyl.resources.resource import Resource


class Variable(Resource):
    def __init__(self, name: str, value: Any):
        super().__init__()
        self._name: str = name
        self._value: Any = value
        self._dtype: type = type(value)

    def operation(self, other, operation):
        if isinstance(other, self.__class__):
            return operation(self._value, other._value)
        return operation(self._value, other)

    def __eq__(self, other):
        return self._name == other._name and self._value == other._value

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
