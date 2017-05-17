import spynnaker7.pyNN as p
from python_models.neuron.builds.if_curr_comb_exp_5E5I import IFCurrCombExp5E5I
import plot_utils
p.setup(0.1)

pop_src1 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0]]}, label="src1")
pop_src2 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0]]}, label="src1")
pop_src3 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0]]}, label="src1")
pop_src4 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0]]}, label="src1")
pop_src5 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0]]}, label="src1")
pop_src6 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0]]}, label="src1")
pop_src7 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0]]}, label="src1")
pop_src8 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0]]}, label="src1")
pop_src9 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0]]}, label="src1")
pop_src10 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0]]}, label="src1")

#IFCurrCombExp.set_excitatory_scalar()

pop_ex = p.Population(1, IFCurrCombExp5E5I, {}, label="test")
#pop_ex.set('inh2_b_tau', 10)

# define the projections
# excitatory

d = 12

exc_proj = p.Projection(pop_src1, pop_ex,
        p.OneToOneConnector(weights=1, delays=1*d), target="excitatory")
exc_proj2 = p.Projection(pop_src2, pop_ex,
        p.OneToOneConnector(weights=1, delays=3*d), target="excitatory2")
exc_proj3 = p.Projection(pop_src3, pop_ex,
        p.OneToOneConnector(weights=1, delays=5*d), target="excitatory3")
exc_proj4 = p.Projection(pop_src4, pop_ex,
        p.OneToOneConnector(weights=1, delays=7*d), target="excitatory4")
exc_proj5 = p.Projection(pop_src5, pop_ex,
        p.OneToOneConnector(weights=1, delays=9*d), target="excitatory5")

inh_proj = p.Projection(pop_src6, pop_ex,
        p.OneToOneConnector(weights=1, delays=2*d), target="inhibitory")
inh_proj2 = p.Projection(pop_src7, pop_ex,
        p.OneToOneConnector(weights=1, delays=4*d), target="inhibitory2")
inh_proj3 = p.Projection(pop_src8, pop_ex,
        p.OneToOneConnector(weights=1, delays=6*d), target="inhibitory3")
inh_proj4 = p.Projection(pop_src9, pop_ex,
        p.OneToOneConnector(weights=1, delays=8*d), target="inhibitory4")
inh_proj5 = p.Projection(pop_src10, pop_ex,
        p.OneToOneConnector(weights=1, delays=10*d), target="inhibitory5")


pop_ex.record()
pop_ex.record_gsyn()
pop_ex.record_v()
p.run(200)

v = pop_ex.get_v()
curr = pop_ex.get_gsyn()
spikes = pop_ex.getSpikes()

plot_utils.plotAll(v, spikes)
plot_utils.plot_gsyn(curr)
p.end()
print "\n job done"