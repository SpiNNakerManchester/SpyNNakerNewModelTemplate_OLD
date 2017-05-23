import spynnaker7.pyNN as p
from python_models.neuron.builds.if_curr_exp_alpha import IFCurrExpAlpha
import plot_utils
p.setup(0.1)

pop_src1 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[1,8, 20]]}, label="src1")

#IFCurrCombExp.set_excitatory_scalar()

pop_ex = p.Population(1, IFCurrExpAlpha, {}, label="test")

# define the projection
exc_proj = p.Projection(pop_src1, pop_ex,
        p.OneToOneConnector(weights=1, delays=1), target="excitatory")

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