from spynnaker.pyNN.utilities.constants import POPULATION_BASED_REGIONS
from spynnaker.pyNN.utilities import utility_calls
from data_specification.enums.data_type import DataType


class MySynapseType(object):
    """
    My Synapse Type
    """
    # noinspection PyPep8Naming
    def __init__(self, n_neurons, machine_time_step,

                 # TODO: Add any parameters
                 my_ex_synapse_parameter=1.0,
                 my_in_synapse_parameter=1.0):

        # TODO: Store any additional parameters
        self._n_neurons = n_neurons
        self._machine_time_step = machine_time_step
        self._my_ex_synapse_parameter = utility_calls.convert_param_to_numpy(
            my_ex_synapse_parameter, n_neurons)
        self._my_in_synapse_parameter = utility_calls.convert_param_to_numpy(
            my_in_synapse_parameter, n_neurons)

    def get_n_synapse_parameters_per_synapse_type(self):

        # TODO: Return the number of parameters
        return 1

    def get_n_synapse_types(self):

        # TODO: Return the number of synapse types
        # (e.g. excitatory and inhibitory)
        return 2

    @staticmethod
    def get_n_synapse_type_bits():

        # TODO: Return the number of bits need to represent the number of
        # synapse types
        return 1

    def write_synapse_parameters(self, spec, subvertex, vertex_slice):
        """
        Write vectors of synapse parameters, one per synapse type per neuron
        """

        # Set the focus to the memory region 3 (synapse parameters):
        spec.switch_write_focus(
            region=POPULATION_BASED_REGIONS.SYNAPSE_PARAMS.value)

        # TODO: Update the following to match the number of synapse types

        # TODO: Update to write the excitatory parameters
        for neuron in range(vertex_slice.n_atoms):
            if self._my_ex_synapse_parameter.size == 1:
                spec.write_value(data=self._my_ex_synapse_parameter[0],
                                 data_type=DataType.S1615)
            else:
                spec.write_value(data=self._my_ex_synapse_parameter[neuron],
                                 data_type=DataType.S1615)

        # TODO: Update to write the inhibitory parameters
        for neuron in range(vertex_slice.n_atoms):
            if self._my_in_synapse_parameter.size == 1:
                spec.write_value(data=self._my_in_synapse_parameter[0],
                                 data_type=DataType.S1615)
            else:
                spec.write_value(data=self._my_in_synapse_parameter[neuron],
                                 data_type=DataType.S1615)
