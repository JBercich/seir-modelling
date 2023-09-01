#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import abc
import typing

from simpyl.core.metaclass import BaseMetaclass


class Resource(BaseMetaclass, abc.ABC):
    """
    Model resource abstraction. Resources are node-like data structure representing an
    element in some system. System models may construct real-life components as a single
    resource or as a collection of different data structures.

    ..NOTE::
        Aliases act to replace the unique identifiaction of resources. If no alias is
        given to a resource, the uuid is used to identify it which is then
    """

    @abc.abstractproperty
    def _alias(self) -> str:
        pass

    def __eq__(self, other):
        if self.get_alias() is not None and other.get_alias() is not None:
            # Instance aliases are equivalent
            return self.get_alias() == other.get_alias()
        return super(self).__eq__(other)

    def __repr__(self):
        if self.get_alias() is not None:
            # Instance alias is appended
            return "{}({})" % (super(self).__repr__(), self.get_alias())
        return super(self).__repr__()

    @typing.final
    def get_alias(self) -> str:
        return self._alias
