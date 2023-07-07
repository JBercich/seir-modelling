from enum import StrEnum

NEURON_INITIAL_MEMBRANE_POTENTIAL: float = -70.0
NEURON_INITIAL_RECOVERY: float = 0.0
NEURON_INPUT_CURRENT: float = 10.0
NEURON_THRESHOLD: float = 30.0


class NeuronName(StrEnum):
    RZ = "Resonator"
    CH = "Chattering"
    FS = "Fast Spiking"
    RS = "Regular Spiking"
    TC = "Thalamo-Cortical"
    IB = "Intrinsically Bursting"
    LTS = "Low-Threshold Spiking"


class NeuronType(StrEnum):
    Other = "Other"
    Excitatory = "Excitatory"
    Inhibitory = "Inhibitory"


class Neuron:
    def __init__(
        self,
        neuron_name: NeuronName,
        neuron_type: NeuronType,
        recovery_time_scale: float,
        recovery_sensitivity: float,
        spike_reset_membrane_potential: float,
        spike_reset_recovery: float,
    ):
        """
        A neuron for the STDP case study is assessed for membrane potential activations
        over a simulated time-delta. Attributes of this instance describe additional
        behaviours of this neuron as the membrane potential and recovery variable change
        over time.

        Args:
            neuron_name (NeuronName): Name of the neuron.
            neuron_type (NeuronType): Type of the neuron.
            recovery_time_scale (float): Time-scale of recovery variable.
            recovery_sensitivity (float): Sensitivity of recovery variable.
            spike_reset_membrane_potential (float): Spike reset of membrane potential.
            spike_reset_recovery (float): Spike reset of recovery variable.
        """
        self.name = neuron_name
        self.type = neuron_type
        self._recovery_time_scale = recovery_time_scale
        self._recovery_sensitivity = recovery_sensitivity
        self._spike_reset_membrane_potential = spike_reset_membrane_potential
        self._spike_reset_recovery = spike_reset_recovery

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def get_name(self):
        return self.name.value

    def get_type(self):
        return self.type.value

    def get_recovery_time_scale(self):
        return self._recovery_time_scale

    def get_recovery_sensitivity(self):
        return self._recovery_sensitivity

    def get_spike_reset_membrane_potential(self):
        return self._spike_reset_membrane_potential

    def get_spike_reset_recovery(self):
        return self._spike_reset_recovery
