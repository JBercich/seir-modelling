#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABC
from dataclasses import dataclass

from simpyl.model.resources.resource import Resource


@dataclass(order=True, slots=True)
class Entity(Resource, ABC):
    alias: str | None = None
