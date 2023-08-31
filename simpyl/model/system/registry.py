#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from uuid import UUID, uuid4
from typing import Any


class Registry:
    def __init__(self, dtype: type):
        self._uuid: UUID = uuid4()
        self._dtype: type = dtype
        self._registry: list[dtype] = []

    def __repr__(self):
        return "{}:{}" % (self.__class__.__name__, self._uuid)

    def __len__(self):
        return len(self.registry)

    def __iter__(self):
        for item in self._registry:
            yield item

    def register(self, item: Any):
        if not isinstance(item, self.dtype):
            raise TypeError(f"{self} does not accept {type(item)}")
        self.registry.append(item)

    def deregister(self, item: Any):
        self.registry.remove(item)
