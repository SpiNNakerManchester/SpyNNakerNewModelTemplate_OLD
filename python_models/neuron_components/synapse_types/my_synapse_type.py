from spynnaker.pyNN.models.neuron.synapse_types.abstract_synapse_type import \
    AbstractSynapseType
from spynnaker.pyNN.utilities import utility_calls
from spynnaker.pyNN.models.neural_properties.neural_parameter \
    import NeuronParameter

from data_specification.enums.data_type import DataType


class MySynapseType(AbstractSynapseType):
    """
    My Synapse Type
    """
    # noinspection PyPep8Naming
    def __init__(self, n_neurons, machine_time_step,

                 # TODO: Add any parameters
                 my_ex_synapse_parameter=1.0,
                 my_in_synapse_parameter=1.0):

        AbstractSynapseType.__init__(self)
        self._n_neurons = n_neurons

        # TODO: Store any additional parameters
        self._machine_time_step = machine_time_step
        self._my_ex_synapse_parameter = utility_calls.convert_param_to_numpy(
            my_ex_synapse_parameter, n_neurons)
        self._my_in_synapse_parameter = utility_calls.convert_param_to_numpy(
            my_in_synapse_parameter, n_neurons)

    def get_n_synapse_parameters_per_synapse_type(self):
        """
        get parameters per synapse types.
        :return:
        """

        # TODO: Return the number of parameters
        return 1

    def get_n_synapse_types(self):
        """
        get the number of different synapse types.
        :return:
        """

        # TODO: Return the number of synapse types
        return 2

    def get_synapse_id_by_target(self, target):
        """
        returns the id by the string target
        :param target: the string target
        :return: id.
        """
        # TODO: update accordingly.

        if target == "excitatory":
            return 0
        elif target == "inhibitory":
            return 1
        return None

    def get_synapse_targets(self):
        """
        returns the different string based targets,
        :return:
        """

        # TODO: update accordingly
        return "excitatory", "inhibitory"

    def get_synapse_type_parameters(self):
        """
        returns the dsg parameter for this synapse type. this has to be
        mapped to the c code.
        :return:
        """
        # TODO: update accordingly.
        return [
            NeuronParameter(self._my_ex_synapse_parameter, DataType.UINT32),
            NeuronParameter(self._my_in_synapse_parameter, DataType.UINT32),
        ]

    def get_n_cpu_cycles_per_neuron(self):
        """
        returns the cpu cycles used per neuron
        :return:
        """
        # TODO: update accordingly.
        return 100
