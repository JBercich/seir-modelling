#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import abc
import dataclasses

from simpyl.model.resources.resource import Resource


ENTITY_FIELD_ORDER: bool = True
ENTITY_WRITE_SLOTS: bool = True


@dataclasses.dataclass(order=ENTITY_FIELD_ORDER, slots=ENTITY_WRITE_SLOTS)
class Entity(Resource, abc.ABC):
    """
    Custom dataclass wrapper for complex, and generally static, simulation variables.

    ..TODO::
        Replace aliasing and built-ins with base dataclasses functionality to reduce the
        required code for this model resource.
    """

    _alias: str = Resource.DEFAULT_ALIAS

    def __repr__(self):
        return super(self).__repr__() + dataclasses.fields(self)

    def __eq__(self, other):
        # Equality function not supported (model hierarchy structure too complicated)
        raise TypeError("unsupported operand type(s) for =: '{}'" % self.__class__)
