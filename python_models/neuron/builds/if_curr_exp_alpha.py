from spynnaker.pyNN.models.neuron.neuron_models\
    .neuron_model_leaky_integrate_and_fire \
    import NeuronModelLeakyIntegrateAndFire
from python_models.neuron.synapse_types.synapse_type_alpha\
    import SynapseTypeAlpha
from spynnaker.pyNN.models.neuron.input_types.input_type_current \
    import InputTypeCurrent
from spynnaker.pyNN.models.neuron.threshold_types.threshold_type_static \
    import ThresholdTypeStatic
from spynnaker.pyNN.models.neuron.abstract_population_vertex \
    import AbstractPopulationVertex
import numpy

class IFCurrExpAlpha(AbstractPopulationVertex):
    """ Leaky integrate and fire neuron with a combined decaying \
        current inputs: synaptic response = Ae^(t/tau_a) + Be^(t/tau_b)
    """

    _model_based_max_atoms_per_core = 255

    default_parameters = {
        'tau_m': 20.0,
        'cm': 1.0,
        'v_rest': -65.0,
        'v_reset': -65.0,
        'v_thresh': -50.0,

        'dt':0.1,
        'exc_response':0,
        'exc_exp_response':0,
        'exc_const_response':0,
        'exc_k':1,
        'exc_t':0.0,
        'exc_tau':2,
        'inh_response':0,
        'inh_exp_response':0,
        'inh_const_response':0,
        'inh_k':1,
        'inh_t':0.0,
        'inh_tau':0.2,

        'tau_refrac': 0.1,
        'i_offset': 0}

    def __init__(
            self, n_neurons, spikes_per_second=None, ring_buffer_sigma=None,
            incoming_spike_buffer_size=None, constraints=None, label=None,
            tau_m=default_parameters['tau_m'], cm=default_parameters['cm'],
            v_rest=default_parameters['v_rest'],
            v_reset=default_parameters['v_reset'],
            v_thresh=default_parameters['v_thresh'],

            dt = default_parameters['dt'],

            exc_response=default_parameters['exc_response'],
            exc_exp_response=default_parameters['exc_exp_response'],
            exc_const_response=default_parameters['exc_const_response'],
            exc_k=default_parameters['exc_k'],
            exc_t=default_parameters['exc_t'],
            exc_tau=default_parameters['exc_tau'],

            inh_response=default_parameters['inh_response'],
            inh_exp_response=default_parameters['inh_exp_response'],
            inh_const_response=default_parameters['inh_const_response'],
            inh_k=default_parameters['inh_k'],
            inh_t=default_parameters['inh_t'],
            inh_tau=default_parameters['inh_tau'],


            tau_refrac=default_parameters['tau_refrac'],
            i_offset=default_parameters['i_offset'], v_init=None):


        # Construct neuron/synapse objects
        neuron_model = NeuronModelLeakyIntegrateAndFire(
            n_neurons, v_init, v_rest, tau_m, cm, i_offset,
            v_reset, tau_refrac)



        synapse_type = SynapseTypeAlpha(
                n_neurons,

                dt,

                exc_response,
                exc_exp_response,
                exc_const_response,
                exc_k,
                exc_t,
                exc_tau,

                inh_response,
                inh_exp_response,
                inh_const_response,
                inh_k,
                inh_t,
                inh_tau
                )


        input_type = InputTypeCurrent()
        threshold_type = ThresholdTypeStatic(n_neurons, v_thresh)

        AbstractPopulationVertex.__init__(
            self, n_neurons=n_neurons, binary="IF_curr_exp_alpha.aplx", label=label,
            max_atoms_per_core=IFCurrExpAlpha._model_based_max_atoms_per_core,
            spikes_per_second=spikes_per_second,
            ring_buffer_sigma=ring_buffer_sigma,
            incoming_spike_buffer_size=incoming_spike_buffer_size,
            model_name="IF_curr_exp_alpha", neuron_model=neuron_model,
            input_type=input_type, synapse_type=synapse_type,
            threshold_type=threshold_type, constraints=constraints)

    @staticmethod
    def set_model_max_atoms_per_core(new_value):
        IFCurrExpAlpha._model_based_max_atoms_per_core = new_value

    @staticmethod
    def get_max_atoms_per_core():
        return IFCurrExpAlpha._model_based_max_atoms_per_core




    @staticmethod
    def calc_rise_time(tau_a, tau_b, A=1, B=-1):
        try:
            return numpy.log((A*tau_b) / (-B*tau_a)) * ( (tau_a*tau_b) / (tau_b - tau_a) )
        except:
            "calculation failed: ensure A!=B and that they are of opposite sign"

    @classmethod
    def calc_scalar_f(cls, tau_a, tau_b):
        t_rise = cls.calc_rise_time(tau_a = tau_a, tau_b=tau_b)
        return 1/(numpy.exp(-t_rise/tau_a) - numpy.exp(-t_rise/tau_b))

    @classmethod
    def set_excitatory_scalar(self, exc_a_tau, exc_b_tau):
        sf = self.calc_scalar_f(tau_a = exc_a_tau, tau_b=exc_b_tau)
        exc_a_A = sf
        exc_b_B = -sf
        return exc_a_A, exc_b_B

