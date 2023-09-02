#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import abc
import dataclasses

from simpyl.model.resources.resource import Resource


ENTITY_FIELD_ORDER: bool = True
ENTITY_WRITE_SLOTS: bool = True


@dataclasses.dataclass(order=ENTITY_FIELD_ORDER, slots=ENTITY_WRITE_SLOTS)
class Entity(Resource, abc.ABC):
    alias: str | None = None
