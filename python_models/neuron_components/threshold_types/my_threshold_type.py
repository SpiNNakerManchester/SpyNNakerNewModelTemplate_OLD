from spynnaker.pyNN.utilities import utility_calls
from spynnaker.pyNN.models.neural_properties.neural_parameter \
    import NeuronParameter
from data_specification.enums.data_type import DataType
from spynnaker.pyNN.models.neuron.threshold_types.abstract_threshold_type \
    import AbstractThresholdType


class MyThresholdType(AbstractThresholdType):
    """ A threshold that is a static value
    """
    def __init__(
            self, n_neurons,

            # TODO: update parameters are required
            my_param_1):
        AbstractThresholdType.__init__(self)
        self._n_neurons = n_neurons

        # TODO: Store any parameters
        self._my_param_1 = utility_calls.convert_param_to_numpy(
            my_param_1, n_neurons)

    def get_n_threshold_parameters(self):
        """
        returns the number of parameters for this threshold type
        :return:
        """
        # TODO: update accordingly.
        return 1

    def get_threshold_parameters(self):
        """
        returns the dsg parameters for this threshold type. must map to the
        order expected by the c code.
        :return:
        """

        # TODO: update accordingly
        return [
            NeuronParameter(self._v_thresh, DataType.S1615)
        ]

    def get_n_cpu_cycles_per_neuron(self):
        """
        returns the cpu cycles per neuron
        :return:
        """

        # TODO: try to guess this.
        return 2
