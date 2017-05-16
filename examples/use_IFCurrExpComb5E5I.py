import spynnaker7.pyNN as p
from python_models.neuron.builds.if_curr_comb_exp_5E5I import IFCurrCombExp5E5I
import plot_utils
p.setup(0.1)

pop_src = p.Population(1, p.SpikeSourceArray, {'spike_times': [[0.1]]}, label="src1")

#IFCurrCombExp.set_excitatory_scalar()

pop_ex = p.Population(1, IFCurrCombExp5E5I, {}, label="test")
pop_ex.set(#'v_thresh',[-54.00, -50, -57, -48, -53.2])
#        'exc_a_response', 0,
#        'exc_a_A',1,
        'exc_a_tau', 0.9)

pop_ex.set('inh2_b_tau', 10)

#        'exc_b_response',0,
#        'exc_b_B',-1,
#        'exc_b_tau', 1.7)

#pop_ex = p.Population(1, p.IF_curr_exp, {}, label="test")


#tau_a = 1.7
#tau_b = 0.2
#t_rise = IFCurrCombExp.calc_rise_time(tau_a, tau_b)
#sf = IFCurrCombExp.calc_scalar_f(tau_a, tau_b)


# define the projection
input_proj = p.Projection(pop_src, pop_ex,
        p.OneToOneConnector(weights=1, delays=1), target="excitatory")
input_proj2 = p.Projection(pop_src, pop_ex,
        p.OneToOneConnector(weights=1, delays=5), target="inhibitory2")


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