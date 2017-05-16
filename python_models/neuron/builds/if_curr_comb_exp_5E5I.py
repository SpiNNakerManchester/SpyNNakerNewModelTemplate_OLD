from spynnaker.pyNN.models.neuron.neuron_models\
    .neuron_model_leaky_integrate_and_fire \
    import NeuronModelLeakyIntegrateAndFire
from python_models.neuron.synapse_types.synapse_type_combined_exponential_5E5I\
    import SynapseTypeCombExp5E5I
from spynnaker.pyNN.models.neuron.input_types.input_type_current \
    import InputTypeCurrent
from spynnaker.pyNN.models.neuron.threshold_types.threshold_type_static \
    import ThresholdTypeStatic
from spynnaker.pyNN.models.neuron.abstract_population_vertex \
    import AbstractPopulationVertex
import numpy

class IFCurrCombExp5E5I(AbstractPopulationVertex):
    """ Leaky integrate and fire neuron with 2 excitatory and 2 inhibitory\
        synapses, each comprised of a combination of exponential functions:\
        synaptic response = Ae^(-t/tau_a) + Be^(-t/tau_b)
    """

    _model_based_max_atoms_per_core = 255

    default_parameters = {
        'tau_m': 20.0,
        'cm': 1.0,
        'v_rest': -65.0,
        'v_reset': -65.0,
        'v_thresh': -50.0,

        ##### synapse parameters #####
        # excitatory
        'exc_response':0,
        'exc_a_response':0,
        'exc_a_A':1,
        'exc_a_tau': 0.2,
        'exc_b_response':0,
        'exc_b_B':-1,
        'exc_b_tau': 1.7,

        # excitatory2
        'exc2_response':0,
        'exc2_a_response':0,
        'exc2_a_A':1,
        'exc2_a_tau': 0.2,
        'exc2_b_response':0,
        'exc2_b_B':-1,
        'exc2_b_tau': 1.7,

        # excitatory3
        'exc3_response':0,
        'exc3_a_response':0,
        'exc3_a_A':1,
        'exc3_a_tau': 0.2,
        'exc3_b_response':0,
        'exc3_b_B':-1,
        'exc3_b_tau': 1.7,

        # excitatory4
        'exc4_response':0,
        'exc4_a_response':0,
        'exc4_a_A':1,
        'exc4_a_tau': 0.2,
        'exc4_b_response':0,
        'exc4_b_B':-1,
        'exc4_b_tau': 1.7,

        # excitatory5
        'exc5_response':0,
        'exc5_a_response':0,
        'exc5_a_A':1,
        'exc5_a_tau': 0.2,
        'exc5_b_response':0,
        'exc5_b_B':-1,
        'exc5_b_tau': 1.7,

        # inhibitory
        'inh_response':0,
        'inh_a_response': 0,
        'inh_a_A':1,
        'inh_a_tau': 0.2,
        'inh_b_response':0,
        'inh_b_B':-1,
        'inh_b_tau': 1.7,

        # inhibitory2
        'inh2_response':0,
        'inh2_a_response': 0,
        'inh2_a_A':1,
        'inh2_a_tau': 0.2,
        'inh2_b_response':0,
        'inh2_b_B':-1,
        'inh2_b_tau': 1.7,

        # inhibitory3
        'inh3_response':0,
        'inh3_a_response': 0,
        'inh3_a_A':1,
        'inh3_a_tau': 0.2,
        'inh3_b_response':0,
        'inh3_b_B':-1,
        'inh3_b_tau': 1.7,

        # inhibitory4
        'inh4_response':0,
        'inh4_a_response': 0,
        'inh4_a_A':1,
        'inh4_a_tau': 0.2,
        'inh4_b_response':0,
        'inh4_b_B':-1,
        'inh4_b_tau': 1.7,

        # inhibitory5
        'inh5_response':0,
        'inh5_a_response': 0,
        'inh5_a_A':1,
        'inh5_a_tau': 0.2,
        'inh5_b_response':0,
        'inh5_b_B':-1,
        'inh5_b_tau': 1.7,


        ##############################

        'tau_refrac': 0.1,
        'i_offset': 0}

    def __init__(
            self, n_neurons, spikes_per_second=None, ring_buffer_sigma=None,
            incoming_spike_buffer_size=None, constraints=None, label=None,
            tau_m=default_parameters['tau_m'], cm=default_parameters['cm'],
            v_rest=default_parameters['v_rest'],
            v_reset=default_parameters['v_reset'],
            v_thresh=default_parameters['v_thresh'],

            # excitatory
            exc_response=default_parameters['exc_response'],
            exc_a_response=default_parameters['exc_a_response'],
            exc_a_A=default_parameters['exc_a_A'],
            exc_a_tau=default_parameters['exc_a_tau'],
            exc_b_response=default_parameters['exc_b_response'],
            exc_b_B=default_parameters['exc_b_B'],
            exc_b_tau=default_parameters['exc_b_tau'],

            # excitatory2
            exc2_response=default_parameters['exc2_response'],
            exc2_a_response=default_parameters['exc2_a_response'],
            exc2_a_A=default_parameters['exc2_a_A'],
            exc2_a_tau=default_parameters['exc2_a_tau'],
            exc2_b_response=default_parameters['exc2_b_response'],
            exc2_b_B=default_parameters['exc2_b_B'],
            exc2_b_tau=default_parameters['exc2_b_tau'],

            # excitatory3
            exc3_response=default_parameters['exc3_response'],
            exc3_a_response=default_parameters['exc3_a_response'],
            exc3_a_A=default_parameters['exc3_a_A'],
            exc3_a_tau=default_parameters['exc3_a_tau'],
            exc3_b_response=default_parameters['exc3_b_response'],
            exc3_b_B=default_parameters['exc3_b_B'],
            exc3_b_tau=default_parameters['exc3_b_tau'],

            # excitatory4
            exc4_response=default_parameters['exc4_response'],
            exc4_a_response=default_parameters['exc4_a_response'],
            exc4_a_A=default_parameters['exc4_a_A'],
            exc4_a_tau=default_parameters['exc4_a_tau'],
            exc4_b_response=default_parameters['exc4_b_response'],
            exc4_b_B=default_parameters['exc4_b_B'],
            exc4_b_tau=default_parameters['exc4_b_tau'],

            # excitatory5
            exc5_response=default_parameters['exc5_response'],
            exc5_a_response=default_parameters['exc5_a_response'],
            exc5_a_A=default_parameters['exc5_a_A'],
            exc5_a_tau=default_parameters['exc5_a_tau'],
            exc5_b_response=default_parameters['exc5_b_response'],
            exc5_b_B=default_parameters['exc5_b_B'],
            exc5_b_tau=default_parameters['exc5_b_tau'],

            # inhibitory
            inh_response=default_parameters['inh_response'],
            inh_a_response=default_parameters['inh_a_response'],
            inh_a_A=default_parameters['inh_a_A'],
            inh_a_tau=default_parameters['inh_a_tau'],
            inh_b_response=default_parameters['inh_b_response'],
            inh_b_B=default_parameters['inh_b_B'],
            inh_b_tau=default_parameters['inh_b_tau'],

            # inhibitory2
            inh2_response=default_parameters['inh2_response'],
            inh2_a_response=default_parameters['inh2_a_response'],
            inh2_a_A=default_parameters['inh2_a_A'],
            inh2_a_tau=default_parameters['inh2_a_tau'],
            inh2_b_response=default_parameters['inh2_b_response'],
            inh2_b_B=default_parameters['inh2_b_B'],
            inh2_b_tau=default_parameters['inh2_b_tau'],

            # inhibitory3
            inh3_response=default_parameters['inh3_response'],
            inh3_a_response=default_parameters['inh3_a_response'],
            inh3_a_A=default_parameters['inh3_a_A'],
            inh3_a_tau=default_parameters['inh3_a_tau'],
            inh3_b_response=default_parameters['inh3_b_response'],
            inh3_b_B=default_parameters['inh3_b_B'],
            inh3_b_tau=default_parameters['inh3_b_tau'],

            # inhibitory4
            inh4_response=default_parameters['inh4_response'],
            inh4_a_response=default_parameters['inh4_a_response'],
            inh4_a_A=default_parameters['inh4_a_A'],
            inh4_a_tau=default_parameters['inh4_a_tau'],
            inh4_b_response=default_parameters['inh4_b_response'],
            inh4_b_B=default_parameters['inh4_b_B'],
            inh4_b_tau=default_parameters['inh4_b_tau'],

            # inhibitory5
            inh5_response=default_parameters['inh5_response'],
            inh5_a_response=default_parameters['inh5_a_response'],
            inh5_a_A=default_parameters['inh5_a_A'],
            inh5_a_tau=default_parameters['inh5_a_tau'],
            inh5_b_response=default_parameters['inh5_b_response'],
            inh5_b_B=default_parameters['inh5_b_B'],
            inh5_b_tau=default_parameters['inh5_b_tau'],

            tau_refrac=default_parameters['tau_refrac'],
            i_offset=default_parameters['i_offset'], v_init=None):


        # Construct neuron/synapse objects
        neuron_model = NeuronModelLeakyIntegrateAndFire(
            n_neurons, v_init, v_rest, tau_m, cm, i_offset,
            v_reset, tau_refrac)

        synapse_type = SynapseTypeCombExp5E5I(
                n_neurons,

                # excitatory
                exc_response,
                exc_a_response,
                exc_a_A,
                exc_a_tau,
                exc_b_response,
                exc_b_B,
                exc_b_tau,

                # excitatory2
                exc2_response,
                exc2_a_response,
                exc2_a_A,
                exc2_a_tau,
                exc2_b_response,
                exc2_b_B,
                exc2_b_tau,

                # excitatory3
                exc3_response,
                exc3_a_response,
                exc3_a_A,
                exc3_a_tau,
                exc3_b_response,
                exc3_b_B,
                exc3_b_tau,

                # excitatory4
                exc4_response,
                exc4_a_response,
                exc4_a_A,
                exc4_a_tau,
                exc4_b_response,
                exc4_b_B,
                exc4_b_tau,

                # excitatory5
                exc5_response,
                exc5_a_response,
                exc5_a_A,
                exc5_a_tau,
                exc5_b_response,
                exc5_b_B,
                exc5_b_tau,

                # inhibitory
                inh_response,
                inh_a_response,
                inh_a_A,
                inh_a_tau,
                inh_b_response,
                inh_b_B,
                inh_b_tau,

                # inhibitory2
                inh2_response,
                inh2_a_response,
                inh2_a_A,
                inh2_a_tau,
                inh2_b_response,
                inh2_b_B,
                inh2_b_tau,

                # inhibitory3
                inh3_response,
                inh3_a_response,
                inh3_a_A,
                inh3_a_tau,
                inh3_b_response,
                inh3_b_B,
                inh3_b_tau,

                # inhibitory4
                inh4_response,
                inh4_a_response,
                inh4_a_A,
                inh4_a_tau,
                inh4_b_response,
                inh4_b_B,
                inh4_b_tau,

                # inhibitory5
                inh5_response,
                inh5_a_response,
                inh5_a_A,
                inh5_a_tau,
                inh5_b_response,
                inh5_b_B,
                inh5_b_tau)

        input_type = InputTypeCurrent()
        threshold_type = ThresholdTypeStatic(n_neurons, v_thresh)

        AbstractPopulationVertex.__init__(
            self, n_neurons=n_neurons, binary="IF_curr_comb_exp_5E5I.aplx", label=label,
            max_atoms_per_core=IFCurrCombExp5E5I._model_based_max_atoms_per_core,
            spikes_per_second=spikes_per_second,
            ring_buffer_sigma=ring_buffer_sigma,
            incoming_spike_buffer_size=incoming_spike_buffer_size,
            model_name="IF_curr_comb_exp_5E5I", neuron_model=neuron_model,
            input_type=input_type, synapse_type=synapse_type,
            threshold_type=threshold_type, constraints=constraints)

    @staticmethod
    def set_model_max_atoms_per_core(new_value):
        IFCurrCombExp5E5I._model_based_max_atoms_per_core = new_value

    @staticmethod
    def get_max_atoms_per_core():
        return IFCurrCombExp5E5I._model_based_max_atoms_per_core

