"""
My model
"""
from spynnaker.pyNN.models.abstract_models.abstract_population_vertex import \
    AbstractPopulationVertex

from spynnaker.pyNN.models.neural_properties.neural_parameter import \
    NeuronParameter

from python_models.neural_models.my_synapse_type import MySynapseType

from data_specification.enums.data_type import DataType


class MyModelCurrMySynapseType(
        # TODO: Inherit from your required components: such as
        # AbstractIntegrateAndFireProperties,

        # This makes the vertex use exponential synapses
        MySynapseType,
        AbstractPopulationVertex):
    """
    MY MDOEL!
    """

    # TODO: edit this to be a unqiue number for your model.
    # This should match the APPLICATION_MAGIC_NUMBER in the Makefile of the C
    # binary.
    CORE_APP_IDENTIFIER = 0x12345679

    # TODO: Set the maximum number of atoms per core that can be supported.
    # For more complex models, you might need to reduce this number.
    _model_based_max_atoms_per_core = 256

    def __init__(self, n_neurons, machine_time_step, timescale_factor,
                 spikes_per_second, ring_buffer_sigma, constraints=None,
                 label=None,

                 # TODO: add extra parameters required by inherited classes
                 my_ex_synapse_parameter=1.0,
                 my_in_synapse_parameter=1.0,

                 # TODO: add extra parameters that you need here
                 v_init=-65.0,
                 i_offset=0.0,
                 my_parameter=1.0
                 ):
        AbstractPopulationVertex.__init__(
            self, n_neurons=n_neurons, label=label,

            # TODO: Replace with the number of parameters to be returned by
            # get_parameters (see below)
            n_params=3,

            # TODO: Replace with the number of parameters to be returned by
            # get_global_parameters (see below)
            n_global_params=1,

            # TODO: fill in this with the name of the c code binary
            binary="my_model_curr_my_synapse_type.aplx",

            # TODO: Ensure any scaling done here matches the scaling done
            # in neuron_model_convert_input in your neuron C code header file
            weight_scale=1.0,

            constraints=constraints,
            max_atoms_per_core=(MyModelCurrMySynapseType
                                ._model_based_max_atoms_per_core),
            machine_time_step=machine_time_step,
            timescale_factor=timescale_factor,
            spikes_per_second=spikes_per_second,
            ring_buffer_sigma=ring_buffer_sigma)
        self._executable_constant = \
            MyModelCurrMySynapseType.CORE_APP_IDENTIFIER
        MySynapseType.__init__(
            self, n_neurons=n_neurons, machine_time_step=machine_time_step,
            my_ex_synapse_parameter=my_ex_synapse_parameter,
            my_in_synapse_parameter=my_in_synapse_parameter)

        # TODO: Instantiate any additional classes inherited from

        # TODO: Store any additional parameters for use in get_parameters
        self._v_init = v_init
        self._i_offset = i_offset
        self._my_parameter = my_parameter

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
        MyModelCurrMySynapseType._model_based_max_atoms_per_core = new_value

    def get_cpu_usage_for_atoms(self, vertex_slice, graph):
        """
        returns how much cpu ticks this model will use to simulate the neuron
        slice from the partitionable vertex.
        :param vertex_slice: the slice of neurons from the partitionable
        vertex that a partitioned vertex is expected to simulate
        :param graph: the partitionable graph object.
        :return: a number of cpu cycles
        """

        # TODO: Attempt to guess how many cpu cycles each atom requires here!
        return 781 * ((vertex_slice.hi_atom - vertex_slice.lo_atom) + 1)

    def get_parameters(self):
        """
        Generates the neural parameters for the C code.
        NEEDS TO BE IN THE SAME ORDER AS THE C CODE EXPECTS
        """

        # TODO: Add any extra parameters here
        return [
            NeuronParameter(self._v_init, DataType.S1615),
            NeuronParameter(self._i_offset, DataType.S1615),
            NeuronParameter(self._my_parameter, DataType.S1615)
        ]

    def is_population_vertex(self):
        """
        helper method for is instance
        :return:
        """
        return True
