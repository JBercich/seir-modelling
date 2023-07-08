from enum import StrEnum

# Neuron behaviour constants
NEURON_INITIAL_POTENTIAL: float = -70.0
NEURON_INITIAL_RECOVERY: float = 0.0
NEURON_STATIC_CURRENT: float = 10.0
NEURON_THRESHOLD: float = 30.0


class NeuronName(StrEnum):
    """
    Neurons have an identifier name in line with Izhikevich's analysis of different
    spike behaviours. Each name corresponds to a specific neuron spike condition set.
    """

    RS = "Regular Spiking"
    IB = "Intrinsically Bursting"
    CH = "Chattering"
    FS = "Fast Spiking"
    LTS = "Low-Threshold Spiking"
    TC = "Thalamo-Cortical"
    RZ = "Resonator"


class NeuronType(StrEnum):
    """
    Neurons have a categorical type. These types describe the biological nature of the
    neuron with respect to how the activity impacts cortical behaviour.
    """

    Excitatory = "Excitatory"
    Inhibitory = "Inhibitory"
    Other = "Other"


class Neuron:
    def __init__(
        self,
        name: NeuronName,
        dtype: NeuronType,
        recovery_time_scale: float,
        recovery_sensitivity: float,
        reset_potential: float,
        reset_recovery: float,
    ):
        """
        A neuron for the STDP case study is assessed for membrane potential activations
        over a simulated time-delta. Attributes of this instance describe additional
        behaviours of this neuron as the membrane potential and recovery variable change
        over time.

        Args:
            name (NeuronName): Name of the neuron.
            dtype (NeuronType): Type of the neuron.
            recovery_time_scale (float): Time-scale of recovery variable.
            recovery_sensitivity (float): Sensitivity of recovery variable.
            reset_potential (float): Spike reset of membrane potential.
            reset_recovery (float): Spike reset of recovery variable.
        """
        self.name: NeuronName = name
        self.dtype: NeuronType = dtype
        self._recovery_time_scale: float = recovery_time_scale
        self._recovery_sensitivity: float = recovery_sensitivity
        self._reset_potential: float = reset_potential
        self._reset_recovery: float = reset_recovery

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def get_name(self) -> str:
        return self.name.value

    def get_dtype(self) -> str:
        return self.dtype.value

    def get_recovery_time_scale(self) -> float:
        return self._recovery_time_scale

    def get_recovery_sensitivity(self) -> float:
        return self._recovery_sensitivity

    def get_reset_potential(self) -> float:
        return self._reset_potential

    def get_reset_recovery(self) -> float:
        return self._reset_recovery
