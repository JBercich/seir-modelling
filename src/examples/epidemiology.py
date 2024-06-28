#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import Any, List

from simgraph import Entity, Constant, SimGraph


import numpy as np


class PopulationSize(Entity):
    def update(
        self,
        recovered_organisms: Entity,
        susceptible_organisms: Entity,
        strain_infected_organisms: List[Entity],
    ) -> Any:
        return (
            recovered_organisms + susceptible_organisms + sum(strain_infected_organisms)
        )


class RecoveredOrganisms(Entity):
    def update(
        self,
        fatality_rate: Constant,
        strain_infected_organisms: List[Entity],
        strain_recovery_rate: List[Entity],
    ) -> Any:
        return -fatality_rate * self + np.sum(
            strain_recovery_rate * strain_infected_organisms
        )


class InfectedOrganisms(Entity):
    def update(
        self,
        population_size: Constant,
        fatality_rate: Constant,
        strain_susceptible_organisms: Entity,
        strain_infection_rate: Constant,
        strain_virulence: Constant,
        strain_recovery_rate: Constant,
    ) -> Any:
        return (
            -fatality_rate * self
            - strain_virulence * self
            + strain_infection_rate
            * self
            * strain_susceptible_organisms
            / population_size
            - strain_recovery_rate * self
        )


class SusceptibleOrganisms(Entity):
    def update(
        self,
        fatality_rate: Constant,
        reproduction_rate: Constant,
        maximum_population: Constant,
        population_size: Constant,
        strain_infected_organisms: List[Entity],
        strain_infection_rate: List[Constant],
    ) -> Any:
        return (
            reproduction_rate
            * population_size
            * (1 - population_size / maximum_population)
            - fatality_rate * self
            - strain_infection_rate * strain_infected_organisms * self / population_size
        )


strain_a_ir = Constant(0.1, name="strain_a_infection_rate")
strain_a_vr = Constant(0.2, name="strain_a_virulence")
strain_a_rr = Constant(0.3, name="strain_a_recovery_rate")
strain_a_infected = InfectedOrganisms(100)
strain_b_ir = Constant(0.01, name="strain_b_infection_rate")
strain_b_vr = Constant(0.02, name="strain_b_virulence")
strain_b_rr = Constant(0.03, name="strain_b_recovery_rate")
strain_b_infected = InfectedOrganisms(200)

susceptible = SusceptibleOrganisms(1000.0, name="susceptible_organisms")
recovered = RecoveredOrganisms(1000.0, name="recovered_organisms")
population_size = PopulationSize(
    susceptible + recovered + strain_a_infected + strain_b_infected,
    name="population_size",
)

reproduction_rate = Constant(0.1, name="reproduction_rate")
fatality_rate = Constant(0.1, name="fatality_rate")
maximum_population = Constant(1000.0, name="maximum_population")

population_size.add_dependencies(
    recovered_organisms=recovered,
    susceptible_organisms=susceptible,
    strain_infected_organisms=[strain_a_infected, strain_b_infected],
)
strain_a_infected.add_dependencies(
    population_size=population_size,
    fatality_rate=fatality_rate,
    strain_susceptible_organisms=susceptible,
    strain_infection_rate=strain_a_ir,
    strain_virulence=strain_a_vr,
    strain_recovery_rate=strain_a_rr,
)
strain_b_infected.add_dependencies(
    population_size=population_size,
    fatality_rate=fatality_rate,
    strain_susceptible_organisms=susceptible,
    strain_infection_rate=strain_b_ir,
    strain_virulence=strain_b_vr,
    strain_recovery_rate=strain_b_rr,
)

recovered.add_dependencies(
    fatality_rate=
    strain_infected_organisms=
    strain_recovery_rate=
)
