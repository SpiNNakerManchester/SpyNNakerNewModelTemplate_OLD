from spynnaker.pyNN.models.neuron.synapse_types.abstract_synapse_type import \
    AbstractSynapseType
from spynnaker.pyNN.utilities import utility_calls
from spynnaker.pyNN.models.neural_properties.neural_parameter \
    import NeuronParameter

from data_specification.enums.data_type import DataType


class MySynapseType(AbstractSynapseType):

    def __init__(self, n_neurons,

                 # TODO: update the parameters
                 my_ex_synapse_parameter=0.1,
                 my_in_synapse_parameter=0.1):

        AbstractSynapseType.__init__(self)
        self._n_neurons = n_neurons

        # TODO: Store the parameters
        self._my_ex_synapse_parameter = utility_calls.convert_param_to_numpy(
            my_ex_synapse_parameter, n_neurons)
        self._my_in_synapse_parameter = utility_calls.convert_param_to_numpy(
            my_in_synapse_parameter, n_neurons)

    def get_n_synapse_types(self):

        # TODO: Update with the number of supported synapse types
        return 2

    def get_synapse_id_by_target(self, target):

        # TODO: update the mapping from name to id
        if target == "excitatory":
            return 0
        elif target == "inhibitory":
            return 1
        return None

    def get_synapse_targets(self):

        # TODO: update to return the same names as above
        return "excitatory", "inhibitory"

    def get_n_synapse_type_parameters(self):

        # TODO: Return the number of parameters
        # Note: This must match the number of parameters in the
        # synapse_param_t data structure in the C code
        return 2

    def get_synapse_type_parameters(self):

        # TODO: update to return the parameters
        # Note: The order of the parameters must match the order in the
        # synapse_param_t data structure in the C code
        return [
            NeuronParameter(self._my_ex_synapse_parameter, DataType.S1615),
            NeuronParameter(self._my_in_synapse_parameter, DataType.S1615),
        ]

    def get_n_cpu_cycles_per_neuron(self):

        # TODO: update to match the number of cycles used by
        # synapse_types_shape_input, synapse_types_add_neuron_input,
        # synapse_types_get_excitatory_input and
        # synapse_types_get_inhibitory_input
        return 100
