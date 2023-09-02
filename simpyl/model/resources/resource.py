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
        given to a resource, the uuid is used.
    """

    DEFAULT_ALIAS: typing.Final[str] = ""

    _alias: str = DEFAULT_ALIAS

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.is_default_alias() and other.is_default_alias():
                # Instance aliases are equivalent
                return self.get_alias() == other.get_alias()
            return super(self).__eq__(other)
        # Invalid type given for equality
        raise TypeError(
            "unsupported operand type(s) for =: '{}' and '{}'"
            % (type(self), type(other))
        )

    def __repr__(self):
        if self.is_default_alias():
            # Instance alias is appended
            return super(self).__repr__() + "({})" % self.get_alias()
        return super(self).__repr__()

    @typing.final
    def get_alias(self) -> str:
        return self._alias

    @typing.final
    def is_default_alias(self) -> bool:
        return self.get_alias().strip() == Resource.DEFAULT_ALIAS
