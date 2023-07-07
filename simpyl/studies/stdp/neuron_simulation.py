import numpy as np
import pandas as pd

from simpyl.studies.stdp.neuron import (
    NEURON_INITIAL_MEMBRANE_POTENTIAL,
    NEURON_INITIAL_RECOVERY,
    NEURON_INPUT_CURRENT,
    NEURON_THRESHOLD,
    Neuron,
)

CURRENT_DELAY_MS: int = 10


class NeuronSimulation:
    @staticmethod
    def step_potential(potential: float, recovery: float, current: float) -> float:
        """
        Update function for a delta time-step of the neuron membrane potential based on
        the previous step value. This uses Izhikevich's formulation of the differential
        equation for the membrane potential.

        $$
        \\frac{dv}{dt} &= 0.04v^2 + 5v + 140 -u + I
        $$

        Args:
            potential (float): Previous updated membrane potential.
            recovery (float): Previous updated recovery variable.
            current (float): Post-synaptic input current.

        Returns:
            float: Delta time-step membrane potential from Izhikevich's formula.
        """
        return (0.04 * potential**2) + (5 * potential) + 150 - recovery + current

    @staticmethod
    def step_recovery(neuron: Neuron, potential: float, recovery: float) -> float:
        """
        Update function for a delta time-step of the neuron recovery based on the
        previous step value. This uses Izhikevich's formulation of the differential
        equation for the recovery variable.

        $$
        \\frac{du}{dt} &= a(bv-u)
        $$

        Args:
            neuron (Neuron): Neuron container for required hyperparameters.
            potential (float): Previous updated membrane potential.
            recovery (float): Previous updated recovery variable.

        Returns:
            float: Delta time-step recovery from Izhikevich's formula.
        """
        recovery_time_scale = neuron.get_recovery_time_scale()
        recovery_sensitivity = neuron.get_recovery_sensitivity()
        return recovery_time_scale * (recovery_sensitivity * potential - recovery)

    @staticmethod
    def simulate_neuron(
        neuron: Neuron,
        ms_timestep: float = 0.1,
        ms_total: int = 1000,
        initial_potential: float = NEURON_INITIAL_MEMBRANE_POTENTIAL,
        initial_recovery: float = NEURON_INITIAL_RECOVERY,
        current_update: float = NEURON_INPUT_CURRENT,
    ) -> pd.DataFrame:
        """
        Simulate the changing membrane potential and recovery variable for an individual
        neuron and given time conditions/input current. This simulation will make time-
        steps based on Izhikevich's differential equations.

        Args:
            neuron (Neuron): Neuron conditions to assess.
            ms_timestep (float, optional): Millisecond delta time-step. Defaults to 0.1.
            ms_total (int, optional): Millisecond simulation time. Defaults to 1000.
            initial_potential (float, optional): Starting membrane potential.
                Defaults to NEURON_INITIAL_MEMBRANE_POTENTIAL.
            initial_recovery (float, optional): Starting recovery variable.
                Defaults to NEURON_INITIAL_RECOVERY.
            current_update (float, optional): Input current for the update step
                differntial equations. Defaults to NEURON_INPUT_CURRENT.

        Returns:
            pd.DataFrame: DataFrame of simulation results. Rows correspond to time step
                with columns for simulation time, membrane potential, and recovery.
        """

        steps = int(ms_total / ms_timestep)

        # Setup containers for recording time-step variable values
        times = np.zeros(steps, dtype=np.float32)
        potential_array = np.zeros(steps, dtype=np.float32)
        recovery_array = np.zeros(steps, dtype=np.float32)
        potential_array[0] = initial_potential
        recovery_array[0] = initial_recovery

        # Cycle through the simulation steps and perform updates
        for index in range(1, steps):
            # Set the input current based on the simulation time
            current = 0 if times[index - 1] < CURRENT_DELAY_MS else current_update

            # Obtain previous values from last time-step
            prev_potential = potential_array[index - 1]
            prev_recovery = recovery_array[index - 1]

            # Account for threshold updates
            if prev_recovery >= NEURON_THRESHOLD:
                reset_potential = neuron.get_spike_reset_membrane_potential()
                reset_recovery = neuron.get_spike_reset_recovery()
                potential_array[index] = reset_potential
                recovery_array[index] = prev_recovery + reset_recovery

            # Otherwise perform normal variable updates
            else:
                new_potential = NeuronSimulation.step_potential(
                    prev_potential, prev_recovery, current
                )
                new_recovery = NeuronSimulation.step_recovery(
                    neuron, prev_potential, prev_recovery
                )
                potential_array[index] = prev_potential + ms_timestep * new_potential
                recovery_array[index] = prev_recovery + ms_timestep * new_recovery

            # Update the time array
            times[index] = times[index - 1] + ms_timestep

        return pd.DataFrame(
            {
                "Time": times,
                "Membrane Potential": potential_array,
                "Recovery Variable": recovery_array,
            }
        )
