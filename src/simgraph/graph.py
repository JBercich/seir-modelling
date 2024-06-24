#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABC, abstractmethod
from uuid import uuid4, UUID
from typing import Any, List, Dict

from simgraph.exceptions import DependencyConflictException

variable_counter: int = 0


class Variable(ABC):

    @classmethod
    def _generate_name(cls, name: str) -> str:
        global variable_counter
        variable_counter += 1
        return f"{name if name else cls.__name__}:{variable_counter - 1}"

    def __init__(self, init: Any = 0, name: str = ""):
        self._id: UUID = uuid4()
        self.value: Any = init
        self._type: Any = type(init)
        self._name: str = self._generate_name(name)
        self.history: List[Any] = [self.value]
        self.depends: Dict[str, Variable] = {}

    def register_dependencies(self, **dependencies):
        for name, variable in dependencies.items():
            if name in self.depends.keys():
                raise DependencyConflictException(name)
            self.depends[name] = variable

    def step(self, *args, **kwargs):
        self.value = self.update(*args, **kwargs, **self.depends)
        if not isinstance(self.value, self._type_value):
            raise TypeError(f"Expected type: {self._type_value}")
        self.history.append(self.value)

    @abstractmethod
    def update(self) -> Any:
        pass


class SimulationGraph:
    def __init__(self):
        self._id: UUID = uuid4()
        self.variables: List[Variable] = []

    def register_variables(self, *variables):
        for variable in variables:
            if not issubclass(type(variable), Variable):
                raise TypeError(f"Requires instances of {Variable}.")
            if variable in self.variables:
                raise ValueError(f"Variable conflict: {variable}")
            self.variables.append(variable)


# class TestVariable(Variable):
#     def update(self):
#         return self.value


# class TestVariable2(Variable):
#     def update(self, dependency):
#         return self.value


# simulation = SimulationGraph()
# var_a = TestVariable()
# var_b = TestVariable()
# var_c = TestVariable2()
# var_c.register_dependencies(dependency=var_b)
# simulation.register_variables(var_a, var_b, var_c)

# print(simulation.variables)
