import spynnaker7.pyNN as p
from python_models.neuron.builds.if_curr_comb_exp import IFCurrCombExp
import plot_utils
p.setup(0.1)

pop_src = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0]]}, label="src1")

#IFCurrCombExp.set_excitatory_scalar()

#pop_ex = p.Population(1, IFCurrCombExp, {}, label="test")
pop_ex = p.Population(1, p.IF_curr_exp, {}, label="test")


#tau_a = 1.7
#tau_b = 0.2
#t_rise = IFCurrCombExp.calc_rise_time(tau_a, tau_b)
#sf = IFCurrCombExp.calc_scalar_f(tau_a, tau_b)


# define the projection
input_proj = p.Projection(pop_src, pop_ex,
        p.OneToOneConnector(weights=1, delays=1), target="excitatory")
#input_proj1 = p.Projection(pop_src, pop_ex, p.OneToOneConnector(weights=100.0, delays=2), target="excitatory_A")

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