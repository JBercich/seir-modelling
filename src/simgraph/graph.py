#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from uuid import uuid4, UUID
from typing import Set

from simgraph.resources import Resource


class SimGraph:
    def __init__(self, name: str = ""):
        self.name: str = name
        self.uuid: UUID = uuid4()
        self.resources: Set[Resource] = set()

    def add_resources(self, *resources) -> None:
        for resource in resources:
            if not issubclass(type(resource), Resource):
                raise TypeError(f"Expected {Resource} but got {type(resource)}")
            self.resources.add(resource)
