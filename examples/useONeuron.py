import spynnaker.pyNN as p
from python_models.neuron.builds.oNeuron import ONeuron

p.setup(1)
p.Population(1, ONeuron, {}, label="oNeuron test")

p.run(10)

