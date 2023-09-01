#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import Any

from simpyl.core.metaclass import BaseMetaclass


class Registry(BaseMetaclass):
    def __init__(self, dtype: type):
        self._dtype: type = dtype
        self._registry: list[dtype] = []

    def __len__(self):
        return len(self.registry)

    def __iter__(self):
        for item in self._registry:
            yield item

    def register(self, item: Any):
        if not isinstance(item, self.dtype):
            raise TypeError(f"{self} does not accept type {type(item)}")
        self.registry.append(item)

    def deregister(self, item: Any):
        self.registry.remove(item)
