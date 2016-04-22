from spynnaker.pyNN.models.neuron.additional_inputs.abstract_additional_input \
    import AbstractAdditionalInput
from spynnaker.pyNN.utilities import utility_calls
from spynnaker.pyNN.models.neural_properties.neural_parameter \
    import NeuronParameter

from data_specification.enums.data_type import DataType


class MyAdditionalInput(AbstractAdditionalInput):
    """ Represents a possible additional independent input for a model
    """

    def __init__(
            self, n_neurons,

            # TODO: update the parameters
            my_param1):

        AbstractAdditionalInput.__init__(self)
        self._n_neurons = n_neurons

        # TODO: update the set of converts to reflect the parameters inputted
        self._param1 = utility_calls.convert_param_to_numpy(
            my_param1, n_neurons)

    def get_n_parameters(self):
        """ Get the number of parameters for the additional input

        :return: The number of parameters
        :rtype: int
        """
        # TODO: update the number of parameters this additional input holds
        return 1

    def get_parameters(self):
        """ Get the parameters for the additional input

        :return: An array of parameters
        :rtype: array of\
                :py:class:`spynnaker.pyNN.models.neural_properties.neural_parameter.NeuronParameter`
        """
        # TODO: need to update this with your parameters.
        return [
            NeuronParameter(self._param1, DataType.S1615),
        ]

    def get_n_cpu_cycles_per_neuron(self):
        """ Get the number of CPU cycles executed by\
            additional_input_get_input_value_as_current and\
            additional_input_has_spiked
        """
        # TODO: need to guess for your model.
        return 10

    def get_sdram_usage_per_neuron_in_bytes(self):
        """ Get the SDRAM usage of this additional input in bytes

        :return: The SDRAM usage
        :rtype: int
        """
        # TODO: need to guess for your model.
        return self.get_n_input_type_parameters() * 4

    def get_dtcm_usage_per_neuron_in_bytes(self):
        """ Get the DTCM usage of this additional input in bytes

        :return: The DTCM usage
        :rtype: int
        """
        # TODO: need to guess for your model.
        return self.get_n_input_type_parameters() * 4
