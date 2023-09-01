#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import abc
import uuid
import typing


class BaseMetaclass(abc.ABC):
    """
    Metaclass for modular package components. Allocates a UUID for any class instance
    and asserts abstract classes cannot be instantiated. Additional class behaviours are
    defined through generic built-ins.

    Usage:
        ```python
        class TestModel(BaseMetaclass):
            def __init__(self):
                assert hasattr(self, "_uuid")
        ```
    """

    _uuid: uuid.UUID

    def __new__(cls, *args, **kwargs):
        # Restrict abstract classes from being instantiated
        if abc.ABC in cls.__bases__:
            raise TypeError("cannot instantiate abstract class")
        # Populate the uuid field for the class instance
        instance: object = super().__new__(cls, *args, **kwargs)
        instance._uuid = uuid.uuid4()
        return instance

    def __eq__(self, other):
        # Equivalence on the instance UUIDs
        return self.get_uuid() == other.get_uuid()

    def __repr__(self):
        # Show the class name and instance UUID
        return f"{self.__class__.__name__}:{self.get_uuid()}"

    def __hash__(self):
        # Instances are unique by UUID making it a suitable hash
        return hash(self.get_uuid())

    @typing.final
    def get_uuid(self) -> uuid.UUID:
        return self._uuid
