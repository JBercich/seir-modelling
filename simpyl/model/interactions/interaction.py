#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import Callable, TypeAlias
from simpyl.model.resources.resource import Resource
from simpyl.model.resources.datafield import DataField

Sources: TypeAlias = list[Resource]
Targets: TypeAlias = list[DataField]
InteractionFn: TypeAlias = Callable[[Sources], Targets]


class Interaction:
    def __init__(self, sources: Sources, targets: Targets, function: InteractionFn):
        self.sources: Sources = sources
        self.targets: Targets = targets
        self.function: InteractionFn = function
