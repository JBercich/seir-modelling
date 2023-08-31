#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABC
from dataclasses import dataclass

from simpyl.resources.resource import Resource


@dataclass(order=True, slots=True)
class Entity(Resource, ABC):
    def __new__(cls, *args, **kwargs):
        if cls == Entity or cls.__bases__[0] == Resource:
            raise TypeError("cannot instantiate abstract class")
        return super(Entity, cls).__new__(cls)
