# Planned Usage

## Example: Neuron Spiking (Continuous)

```python
from simpyl import Variable, Element, SystemModel

# Define objects
class Neuron(Element):
    a: float
    b: float
    c: float
    d: float
    r: float
neuron: Neuron = Neuron(1., 2., 3., 4., 5.)
membrane_potential: Variable = Variable("Membrane Potential", 10.1, dtype=float, max_value=100, ...)
potential_reset: Variable = Variable("Neuron Reset", 0.)

# Define system updates
@SystemModel.continuous(timestep=0.1)
def update_membrane_potential(neuron: Neuron, membrane_potential: Variable):
    return neuron.a * neuron.b * (membrane_potential * 2)

@SystemModel.continuous(timestep=0.2)
def update_potential_reset(neuron, membrane_potential, potential_reset):
    return ...

# Perform the simulation
simulation = SystemModel.run(lifetime=1000)
```
