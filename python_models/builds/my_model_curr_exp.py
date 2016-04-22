"""
My model
"""
# main interface to use the spynnaker related tools.
# ALL MODELS MUST INHERIT FROM THIS
from spynnaker.pyNN.models.neuron.abstract_population_vertex import \
    AbstractPopulationVertex


# TODO: additional inputs (import as required)
# There are no standard models for this, so import your own
from python_models.neuron_components.additional_inputs.my_additional_input \
    import MyAdditionalInput

# TODO: input types (all imported for help, only use one)
# standard
from spynnaker.pyNN.models.neuron.input_types.input_type_current import \
    InputTypeCurrent
from spynnaker.pyNN.models.neuron.input_types.input_type_conductance \
    import InputTypeConductance
# new model template
from python_models.neuron_components.input_types.my_input_type \
    import MyInputType

# TODO: neuron models (all imported for help, only use one)
# standard
from spynnaker.pyNN.models.neuron.neuron_models.\
    neuron_model_leaky_integrate_and_fire \
    import NeuronModelLeakyIntegrateAndFire
from spynnaker.pyNN.models.neuron.neuron_models.neuron_model_leaky_integrate \
    import NeuronModelLeakyIntegrate
from spynnaker.pyNN.models.neuron.neuron_models.neuron_model_izh \
    import NeuronModelIzh
# new model template
from python_models.neuron_components.neuron_model.my_neuron_model \
    import MyNeuronModel

# TODO: synapse types (all imported for help, only use one)
# standard
from spynnaker.pyNN.models.neuron.synapse_types.synapse_type_exponential \
    import SynapseTypeExponential
from spynnaker.pyNN.models.neuron.synapse_types.synapse_type_dual_exponential \
    import SynapseTypeDualExponential
# new model template
from python_models.neuron_components.synapse_types.my_synapse_type \
    import MySynapseType


# threshold types (all imported for help, only use one)
# standard
from spynnaker.pyNN.models.neuron.threshold_types.threshold_type_static \
    import ThresholdTypeStatic
# new model template
from python_models.neuron_components.threshold_types.my_threshold_type\
    import MyThresholdType


class MyModelCurrExp(AbstractPopulationVertex):
    """
    MY MODEL!
    """

    # TODO: Set the maximum number of atoms per core that can be supported.
    # For more complex models, you might need to reduce this number.
    _model_based_max_atoms_per_core = 256

    # TODO: update accordingly
    # default parameters for this build. Used when end user has not entered any
    default_parameters = {
        'tau_m': 20.0, 'cm': 1.0, 'v_rest': -65.0, 'v_reset': -65.0,
        'v_thresh': -50.0, 'tau_syn_E': 5.0, 'tau_syn_I': 5.0,
        'tau_refrac': 0.1, 'i_offset': 0}

    def __init__(
            self, n_neurons, machine_time_step, timescale_factor,
            spikes_per_second=None, ring_buffer_sigma=None,
            incoming_spike_buffer_size=None, constraints=None, label=None,

            # TODO: neuron model parameters (add / remove as required)
            # neuron model parameters
            tau_refrac=default_parameters['tau_refrac'],
            i_offset=default_parameters['i_offset'],
            tau_m=default_parameters['tau_m'],
            cm=default_parameters['cm'],
            v_rest=default_parameters['v_rest'],
            v_reset=default_parameters['v_reset'],

            # TODO: threshold types parameters (add / remove as required)
            # threshold types parameters
            v_thresh=default_parameters['v_thresh'],

            # TODO: synapse type parameters (add /remove as required)
            # synapse type parameters
            tau_syn_E=default_parameters['tau_syn_E'],
            tau_syn_I=default_parameters['tau_syn_I'],

            # TODO: input type parameters (add / remove as required)
            # additional input type parameters

            # TODO: add extra parameters that you need here
            # additional parameters that this model requires.
            my_parameter=1.0, v_init=None):

        # TODO: create your neuron model class (change if required)
        # create your neuron model class
        neuron_model = NeuronModelLeakyIntegrateAndFire(
            n_neurons, machine_time_step, v_init, v_rest, tau_m, cm, i_offset,
            v_reset, tau_refrac)

        # TODO: create your synapse type model class (change if required)
        # create your synapse type model
        synapse_type = SynapseTypeExponential(
            n_neurons, machine_time_step, tau_syn_E, tau_syn_I)

        # TODO: create your input type model class (change if required)
        # create your input type model
        input_type = InputTypeCurrent()

        # TODO: create your threshold type model class (change if required)
        # create your threshold type model
        threshold_type = ThresholdTypeStatic(n_neurons, v_thresh)

        # TODO: create your own additional inputs (change if required).
        # create your own additional inputs
        additional_input = None

        # instantiate the sPyNNaker system by initializing
        #  the AbstractPopulationVertex
        AbstractPopulationVertex.__init__(
            # standard inputs, do not need to change.
            self, n_neurons=n_neurons, label=label,
            max_atoms_per_core=MyModelCurrExp._model_based_max_atoms_per_core,
            machine_time_step=machine_time_step,
            timescale_factor=timescale_factor,
            spikes_per_second=spikes_per_second,
            ring_buffer_sigma=ring_buffer_sigma,
            incoming_spike_buffer_size=incoming_spike_buffer_size,
            neuron_model=neuron_model, input_type=input_type,
            synapse_type=synapse_type, threshold_type=threshold_type,
            additional_input=additional_input,
            model_name=self.model_name, binary=self._binary_name)

        # TODO: Store any additional parameters for use in get_parameters
        self._my_parameter = my_parameter

    @property
    def _binary_name(self):
        # TODO: edit this to be the name of your compiled c code.
        return "my_model_curr_exp.aplx"

    @property
    def model_name(self):
        """
        returns the name of this model in a human readable form
        :return:
        """

        # TODO: Edit this to be the name of your model in a human readable form
        return "MyModel"

    @staticmethod
    def set_model_max_atoms_per_core(new_value):
        """
        is a hard method needed for spynnaker to allow pynn
        scripts to control the max atoms per core on a model scope.
        :param new_value: the new max atoms per core for this model
        :return:None
        """
        MyModelCurrExp._model_based_max_atoms_per_core = new_value
