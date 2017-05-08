import spynnaker.pyNN as p
from python_models.neuron.builds.if_curr_exp_diff import IFCurrExpDiff
import plot_utils
p.setup(1)

pop_src = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0]]}, label="src1")

pop_ex = p.Population(1, IFCurrExpDiff, {}, label="test")


# define the projection
input_proj = p.Projection(pop_src, pop_ex,
        p.OneToOneConnector(weights=10.0, delays=1), target="excitatory")
#input_proj1 = p.Projection(pop_src, pop_ex, p.OneToOneConnector(weights=100.0, delays=2), target="excitatory_A")

pop_ex.record()
pop_ex.record_v()
p.run(100)

v = pop_ex.get_v()
spikes = pop_ex.getSpikes()

plot_utils.plotAll(v, spikes)

print "job done"