from spynnaker.pyNN.models.neural_properties.neural_parameter \
    import NeuronParameter
from spynnaker.pyNN.models.neuron.neuron_models.abstract_neuron_model \
    import AbstractNeuronModel
from spynnaker.pyNN.utilities import utility_calls

from data_specification.enums.data_type import DataType


class MyNeuronModel(AbstractNeuronModel):
    """
    the neuron modelling part of the neuron
    """

    def __init__(
            self, n_neurons, machine_time_step,

            # TODO: update with params as needed
            my_param_1):
        AbstractNeuronModel.__init__(self)
        self._n_neurons = n_neurons
        self._machine_time_step = machine_time_step

        # TODO: Store any parameters
        self._my_param_1 = \
            utility_calls.convert_param_to_numpy(my_param_1, n_neurons)


    def get_n_neural_parameters(self):
        """
        returns the number of parameters used by this model
        :return:
        """
        # TODO: update accordingly
        return 1

    def get_neural_parameters(self):
        """
        returns the parameters used by the dsg. must be mapped to c code.
        These parameters are the ones which repeat per neuron
        :return: list of neuron parameters
        """

        # TODO: update accordingly
        return [

            # membrane voltage [mV]
            # REAL     V_membrane;
            NeuronParameter(self._v_init, DataType.S1615),

            # membrane resting voltage [mV]
            # REAL     V_rest;
            NeuronParameter(self._v_rest, DataType.S1615),

            # membrane resistance [MOhm]
            # REAL     R_membrane;
            NeuronParameter(self._r_membrane, DataType.S1615),

            # 'fixed' computation parameter - time constant multiplier for
            # closed-form solution
            # exp( -(machine time step in ms)/(R * C) ) [.]
            # REAL     exp_TC;
            NeuronParameter(self._exp_tc, DataType.S1615),

            # offset current [nA]
            # REAL     I_offset;
            NeuronParameter(self._i_offset, DataType.S1615)
        ]

    def get_n_global_parameters(self):
        """
        return the number of parameters which are not neuron specific
        :return:
        """

        # TODO: update accordingly
        return 0

    def get_global_parameters(self):
        """
        returns the global parameters for DSG, must be linked to c code.
        :return:
        """

        # TODO: update accordingly
        return []

    def get_n_cpu_cycles_per_neuron(self):
        """
        returns the number of cpu cycles each neuron should take per timer tick
        :return:
        """
        # TODO: guess
        return 80
