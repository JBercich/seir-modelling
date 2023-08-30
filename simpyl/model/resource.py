#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import Any
from uuid import UUID, uuid4
from abc import ABC
from dataclasses import dataclass


class Resource(ABC):
    def __init__(self):
        self._uuid: UUID = uuid4()

    def __repr__(self):
        return f"{self.__class__.__name__}:{self._uuid}"

    def __eq__(self, other):
        return self._uuid == other._uuid

    def __hash__(self):
        return hash(self._uuid)


class Variable(Resource):
    def __init__(self, name: str, value: Any):
        super().__init__()
        self._name = name
        self._value = value
        self._dtype = type(value)


@dataclass(order=True, slots=True)
class Element(ABC):
    def __new__(cls, *args, **kwargs):
        if cls == Element or cls.__bases__[0] == Element:
            raise TypeError("cannot instantiate abstract class")
        return super().__new__(cls)


print(Variable("test", 1))
print(Variable("test", 2))
print(Variable("test", 3))


class FunDecorator:
    def __init__(self):
        self.registry = []

    def __call__(self, m):
        "This method is called when some method is decorated"
        self.registry.append(m)  # Add function/method to the registry

        def w(my_arg):
            print(my_arg, m)

        return w


run_this_method = FunDecorator()  # Create class instance to be used as decorator


@run_this_method
def method_with_custom_name(my_arg):
    return "The args is: " + my_arg


# do some magic with each decorated method:
for m in run_this_method.registry:
    print(m.__name__)
