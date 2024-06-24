#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from simgraph import Entity, Constant, SimGraph

# @staticmethod
# def step_num_susceptible(
#     env: Environment,
#     population_size: float,
#     num_susceptible: float,
#     num_infected: np.ndarray,
#     strain_infection_rate: np.ndarray,
# ) -> np.ndarray:
#     return (
#         env.reproduction_rate
#         * population_size
#         * (1 - population_size / env.maximum_population)
#         - env.fatality_rate * num_susceptible
#         - np.sum(
#             strain_infection_rate * num_infected * num_susceptible / population_size
#         )
#     )

# @staticmethod
# def step_num_infected(
#     env: Environment,
#     population_size: float,
#     num_susceptible: float,
#     num_infected: np.ndarray,
#     strain_infection_rate: np.ndarray,
#     strain_virulence: np.ndarray,
#     strain_recovery_rate: np.ndarray,
# ) -> np.ndarray:
#     return (
#         -env.fatality_rate * num_infected
#         - strain_virulence * num_infected
#         + strain_infection_rate * num_infected * num_susceptible / population_size
#         - strain_recovery_rate * num_infected
#     )

# @staticmethod
# def step_num_recovered(
#     env: Environment,
#     num_infected: np.ndarray,
#     num_recovered: float,
#     strain_recovery_rate: np.ndarray,
# ):

import numpy as np


class RecoveredOrganisms(Entity):
    def update(
        self,
        fatality_rate: float,
        strain_infected_organisms: np.ndarray,
        strain_recovery_rate: np.ndarray,
    ) -> float:
        return -fatality_rate * self + np.sum(
            strain_recovery_rate * strain_infected_organisms
        )


# Make iterables possible as grouped dependencies

# from dataclasses import dataclass


# @dataclass
# class Strain:
#     infection_rate: float
#     virulence: float
#     recovery_rate: float


# @dataclass
# class Infection:
#     strain: Strain
#     num_infected: float


# @dataclass
# class Environment:
#     reproduction_rate: float
#     fatality_rate: float
#     maximum_population: float


# @dataclass
# class SEIR:
#     infections: list[Infection]
#     num_susceptible: float
#     num_recovered: float


# result: pl.DataFrame = SEIRSimulation(
#     Environment(0.1, 0.1, 1000.0),
#     SEIR(
#         [
#             Infection(Strain(0.1, 0.2, 0.3), 100.0),
#             Infection(Strain(0.01, 0.02, 0.03), 200.0),
#         ],
#         1000.0,
#         1000.0,
#     ),
# ).run(100000, 0.1)

# print(result)
# print(time.time() - t0)
