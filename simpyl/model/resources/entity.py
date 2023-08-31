#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABC
from dataclasses import dataclass

from simpyl.system.resources import Resource


@dataclass(order=True, slots=True)
class Entity(Resource, ABC):
    pass
