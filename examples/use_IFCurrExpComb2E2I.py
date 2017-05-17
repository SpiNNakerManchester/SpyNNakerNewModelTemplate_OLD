import spynnaker7.pyNN as p
from python_models.neuron.builds.if_curr_comb_exp_2E2I import IFCurrCombExp2E2I
import plot_utils
p.setup(0.1)

pop_src1 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[1]]}, label="src1")
#pop_src2 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[1]]}, label="src2")
#pop_src3 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[1]]}, label="src3")
#pop_src4 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[1]]}, label="src4")

#IFCurrCombExp.set_excitatory_scalar()

pop_ex = p.Population(1, IFCurrCombExp2E2I, {}, label="test")

# define the projection
exc_proj = p.Projection(pop_src1, pop_ex,
        p.OneToOneConnector(weights=1, delays=10), target="excitatory")

exc2_proj = p.Projection(pop_src1, pop_ex,
        p.OneToOneConnector(weights=1, delays=30), target="excitatory2")

inh_proj = p.Projection(pop_src1, pop_ex,
        p.OneToOneConnector(weights=1, delays=20), target="inhibitory")

inh2_proj2 = p.Projection(pop_src1, pop_ex,
        p.OneToOneConnector(weights=1, delays=40), target="inhibitory2")


pop_ex.record()
pop_ex.record_gsyn()
pop_ex.record_v()
p.run(50)

v = pop_ex.get_v()
curr = pop_ex.get_gsyn()
spikes = pop_ex.getSpikes()

plot_utils.plotAll(v, spikes)
plot_utils.plot_gsyn(curr)
p.end()
print "\n job done"