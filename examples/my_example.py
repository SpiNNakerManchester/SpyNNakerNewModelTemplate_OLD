import pylab

import spynnaker.pyNN as p
from python_models.builds.my_model_curr_exp import MyModelCurrExp
from python_models.neuron.builds.my_model_curr_my_synapse_type \
    import MyModelCurrMySynapseType


# Set the run time of the execution
run_time = 1000

# Set the time step of the simulation in milliseconds
time_step = 1.0

# Set the number of neurons to simulate
n_neurons = 1

# Set the i_offset current
i_offset = 0.0

# Set the weight of input spikes
weight = 2.0

# Set the times at which to input a spike
spike_times = range(0, run_time, 100)

# A function to create a graph of voltage against time
def create_v_graph(population, title):
    v = population.get_v()
    if v is not None:
        ticks = len(v) / n_neurons
        pylab.figure()
        pylab.xlabel('Time (ms)')
        pylab.ylabel("Membrane Voltage")
        pylab.title(title)

        for pos in range(n_neurons):
            v_for_neuron = v[pos * ticks: (pos + 1) * ticks]
            pylab.plot([i[1] for i in v_for_neuron],
                       [i[2] for i in v_for_neuron])

p.setup(time_step)

input_pop = p.Population(
    1, p.SpikeSourceArray, {"spike_times": spike_times}, label="input")

my_model_pop = p.Population(
    1, MyModelCurrExp,
    {"my_parameter": 2.0,
     "i_offset": i_offset},
    label="my_model_pop")
p.Projection(input_pop, my_model_pop, p.OneToOneConnector(weights=weight))

my_model_my_synapse_type_pop = p.Population(
    1, MyModelCurrMySynapseType,
    {"my_parameter": 3.0,
     "i_offset": i_offset,
     "my_ex_synapse_parameter": 1.0,
     "my_in_synapse_parameter": 2.0},
    label="my_model_my_synapse_type_pop")
p.Projection(input_pop, my_model_my_synapse_type_pop,
             p.OneToOneConnector(weights=weight))

my_model_pop.record_v()
my_model_my_synapse_type_pop.record_v()

p.run(run_time)

create_v_graph(my_model_pop, "My Model")
create_v_graph(my_model_my_synapse_type_pop, "My Model with My Synapse Type")
pylab.show()
