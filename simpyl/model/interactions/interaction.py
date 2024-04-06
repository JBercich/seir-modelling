#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import typing
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

    def run(self) -> dict[DataField, typing.Any]:
        return {t: v for v, t in zip(*self.function(*self.sources), self.targets)}
