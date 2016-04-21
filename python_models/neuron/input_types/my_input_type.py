from data_specification.enums.data_type import DataType
from spynnaker.pyNN.utilities import utility_calls
from spynnaker.pyNN.models.neural_properties.neural_parameter \
    import NeuronParameter
from spynnaker.pyNN.models.neuron.input_types.abstract_input_type \
    import AbstractInputType


class MyInputType(AbstractInputType):
    """
    my input type
    """

    def __init__(
            self, n_neurons,

            # TODO: add extra params / rename these ones
            my_additional_input_param1,
            my_additional_input_param2):

        AbstractInputType.__init__(self)
        self._n_neurons = n_neurons

        # TODO: store your parameters in some private variables
        self._my_additional_input_param1 = \
            utility_calls.convert_param_to_numpy(
                my_additional_input_param1, n_neurons)
        self._my_additional_input_param2 = \
            utility_calls.convert_param_to_numpy(
                my_additional_input_param2, n_neurons)

    def get_global_weight_scale(self):
        """
        returns the weight scale for this input type
        :return:
        """
        # TODO: calculate your weight scaling value here.
        return 1024.0

    def get_n_input_type_parameters(self):
        """
        returns the number of parameters required by this input type.
        :return:
        """
        # TODO: update this value to reflect the number of parameters used by this input type.
        return 2

    def get_input_type_parameters(self):
        """
        returns the input parameters in a form used by the DSG. this order
        needs to be reflected within the c code.
        :return:
        """
        # TODO: need to update this with your parameters.
        return [
            NeuronParameter(self._my_additional_input_param1, DataType.S1615),
            NeuronParameter(self._my_additional_input_param2, DataType.S1615)
        ]

    def get_n_cpu_cycles_per_neuron(self, n_synapse_types):
        """
        returns the number of CPU cycles each neuron uses given the
        number of synapse types
        :param n_synapse_types:
        :return:
        """

        # TODO: need to guess for your model.
        return 10
