#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from uuid import UUID, uuid4
from abc import ABC

from simpyl.system import BaseMetaclass


class Resource(BaseMetaclass, ABC):
    def __new__(cls, *args, **kwargs):
        if cls == Resource or cls.__bases__[0] == ABC:
            raise TypeError("cannot instantiate abstract class")
        return super(Resource, cls).__new__(cls)
