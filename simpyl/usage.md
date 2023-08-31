# Planned Usage

## Example: Neuron Spiking (Continuous)

```python

# Construction of the model resources

class Neuron(Resource):
    a: int
    b: int

neuron = Neuron(1, 2)

neuron_memb = Resource(name="MEMB", value=100, ...)
neuron_updt = Resource(name="UPDT", value=250, ...)


# Register interactions

## Global scope model

model1 = Model()

@model1.register.continuous(neuron, neuron_memb=neuron_memb, target=neuron_memb, timestep=0.1,...)
def update_memb(neuron, neuron_memb) -> Any:
    return neuron.a * neuron.b ** neuron_memb

simulation = model1.run()


## Local scope model

def update_updt(neuron, neuron_updt) -> Any:
    return neuron.a * neuron.b ** neuron_updt

model2 = Model()
model2.register.continuous(neuron_updt, timestep=0.5, target=update_updt, neuron=neuron, ...)
simulation = model2.run()
```
