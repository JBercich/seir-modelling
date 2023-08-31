#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import abc
import uuid


class BaseMetaclass(abc.ABC):
    """
    Superclass for system abstraction elements providing OOP functionality like stopping
    any abstract classes from being instantiated and auto-generating a uuuid for any
    instance of a subclass. Generic built-ins are defined to minimise code repetition.
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
        return self.get_uuid() == other.get_uuid()

    def __repr__(self):
        return f"{self.__class__.__name__}:{self.get_uuid()}"

    def __hash__(self):
        return hash(self.get_uuid())

    def get_uuid(self):
        return self._uuid
