#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import operator
from typing import Any
from uuid import UUID, uuid4
from abc import ABC
from dataclasses import dataclass


class Resource(ABC):
    def __new__(cls, *args, **kwargs):
        if cls == Resource or cls.__bases__[0] == ABC:
            raise TypeError("cannot instantiate abstract class")
        return super().__new__(cls)

    def __init__(self):
        self._uuid: UUID = uuid4()

    def __repr__(self):
        clsname: str = self.__class__.__name__
        cls_uuid: UUID = self._uuid
        return f"{clsname}:{cls_uuid}"

    def __eq__(self, other):
        return self._uuid == other._uuid

    def __hash__(self):
        return hash(self._uuid)


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


@dataclass(order=True, slots=True)
class Element(ABC):
    def __new__(cls, *args, **kwargs):
        if cls == Element or cls.__bases__[0] == Element:
            raise TypeError("cannot instantiate abstract class")
        return super().__new__(cls, *args, **kwargs)


# class FunDecorator:
#     def __init__(self):
#         self.registry = []

#     def __call__(self, m):
#         "This method is called when some method is decorated"
#         self.registry.append(m)  # Add function/method to the registry

#         def w(my_arg):
#             print(my_arg, m)

#         return w


# run_this_method = FunDecorator()  # Create class instance to be used as decorator


# @run_this_method
# def method_with_custom_name(my_arg):
#     return "The args is: " + my_arg


# # do some magic with each decorated method:
# for m in run_this_method.registry:
#     print(m.__name__)
