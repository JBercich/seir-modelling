# Model

Models describe a singular system consisting of resources and interactions. Behaviours of the model are assessed over time-based or event-based simulations. This abstraction of model can allow more flexibility when constructing a simulation and allow easier differentiation between the many types.

## Abstraction Overview

### Resources

A resource contains information with attached metadata in different forms for convenient model construction. The data contained in a resource will differ depending on the model being constructed but is designed to be highly modular and flexible when designing the system model.

#### Variables

A variable is a type of resource that stores a single value. These are tracked values in a simulation which can be updated per some time-step cycle. Variables have additional functionality to allow for default operators that are used on its native type to be applied as if only the value is in that operation.

#### Entities

Entities are contains for multiple named values or variables for convenient abtractions of system logic. This condenses the required resources used within an interaciton.

### Interactions

Interactions are functions that take as input some set of parameters that are all resources, and a target variable(s) that are given by some update value. As in, the function produces a value(s) for some target(s) which are updated with respect to a wrapper simulation for the model.

### Models

Work in progress.
