#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from dataclasses import dataclass


@dataclass
class Strain:
    infection_rate: float
    virulence: float
    recovery_rate: float


@dataclass
class Environment:
    reproduction_rate: float
    fatality_rate: float
    maximum_population: float
    strains: list[Strain]


@dataclass
class SEIR:
    num_infected: dict[Strain, float]
    num_susceptible: float
    num_recovered: float
