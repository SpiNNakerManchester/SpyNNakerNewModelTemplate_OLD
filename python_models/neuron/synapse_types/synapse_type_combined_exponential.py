from pacman.executor.injection_decorator import inject_items
from spynnaker.pyNN.models.neuron.synapse_types.synapse_type_exponential \
    import get_exponential_decay_and_init

from spynnaker.pyNN.models.neuron.synapse_types.abstract_synapse_type import \
    AbstractSynapseType
from spynnaker.pyNN.utilities import utility_calls
from spynnaker.pyNN.models.neural_properties.neural_parameter \
    import NeuronParameter

from data_specification.enums.data_type import DataType
from enum import Enum
class _DIFF_EXP_TYPES(Enum):
    E_RESPONSE = (1, DataType.S1615)

    E_A_RESPONSE = (2, DataType.S1615)
    E_A_A = (3, DataType.S1615)
    E_A_DECAY = (4, DataType.UINT32)
    E_A_INIT = (5, DataType.UINT32)

    E_B_RESPONSE = (6, DataType.S1615)
    E_B_B = (7, DataType.S1615)
    E_B_DECAY = (8, DataType.UINT32)
    E_B_INIT = (9, DataType.UINT32)

    I_DECAY = (10, DataType.UINT32)
    I_INIT = (11, DataType.UINT32)
    I_RESPONSE = (12, DataType.S1615)

    def __new__(cls, value, data_type):
        obj = object.__new__(cls)
        obj._value_ = value
        obj._data_type = data_type
        return obj

    @property
    def data_type(self):
        return self._data_type


class SynapseTypeCombinedExponential(AbstractSynapseType):

    def __init__(self,
                n_neurons,

                exc_response,

                exc_a_response,
                exc_a_A,
                exc_a_tau,

                exc_b_response,
                exc_b_B,
                exc_b_tau,

                inh_response,
                inh_tau):

        AbstractSynapseType.__init__(self)
        self._n_neurons = n_neurons

        self._exc_response = utility_calls.convert_param_to_numpy(exc_response, n_neurons)

        self._exc_a_response = utility_calls.convert_param_to_numpy(exc_a_response, n_neurons)
        self._exc_a_A = utility_calls.convert_param_to_numpy(exc_a_A, n_neurons)
        self._exc_a_tau = utility_calls.convert_param_to_numpy(exc_a_tau, n_neurons)

        self._exc_b_response = utility_calls.convert_param_to_numpy(exc_b_response, n_neurons)
        self._exc_b_B = utility_calls.convert_param_to_numpy(exc_b_B, n_neurons)
        self._exc_b_tau = utility_calls.convert_param_to_numpy(exc_b_tau, n_neurons)

        self._inh_tau = utility_calls.convert_param_to_numpy(inh_tau, n_neurons)
        self._inh_response = utility_calls.convert_param_to_numpy(inh_response, n_neurons)


    @property
    def exc_inp_buf_val(self):
        return self._exc_inp_buf_val

    @exc_inp_buf_val.setter
    def exc_inp_buf_val(self, exc_inp_buf_val):
        self._exc_inp_buf_val = utility_calls.convert_param_to_numpy(
            exc_inp_buf_val, self._n_neurons)

    @property
    def exc_a_response(self):
        return self._exc_a_response

    @exc_a_response.setter
    def exc_a_response(self, exc_a_response):
        self._exc_a_response = utility_calls.convert_param_to_numpy(
            exc_a_response, self._n_neurons)

    @property
    def exc_a_A(self):
        return self._exc_a_A

    @exc_a_A.setter
    def exc_a_A(self, exc_a_tau):
        self._exc_a_A = utility_calls.convert_param_to_numpy(
            exc_a_A, self._n_neurons)

    @property
    def exc_a_tau(self):
        return self._exc_a_tau

    @exc_a_tau.setter
    def exc_a_tau(self, exc_a_tau):
        self._exc_a_tau = utility_calls.convert_param_to_numpy(
            exc_a_tau, self._n_neurons)

    @property
    def exc_b_response(self):
        return self._exc_b_response

    @exc_b_response.setter
    def exc_b_response(self, exc_b_response):
        self._exc_b_response = utility_calls.convert_param_to_numpy(
            exc_b_response, self._n_neurons)

    @property
    def exc_b_B(self):
        return self._exc_b_B

    @exc_b_B.setter
    def exc_b_B(self, exc_b_B):
        self._exc_b_B = utility_calls.convert_param_to_numpy(
            exc_b_B, self._n_neurons)

    @property
    def exc_b_tau(self):
        return self._exc_b_tau

    @exc_b_tau.setter
    def exc_b_tau(self, exc_b_tau):
        self._exc_b_tau = utility_calls.convert_param_to_numpy(
            exc_b_tau, self._n_neurons)


    @property
    def inh_response(self):
        return self._inh_tau

    @inh_response.setter
    def inh_response(self, inh_response):
        self._inh_response = utility_calls.convert_param_to_numpy(
            inh_response, self._n_neurons)

    @property
    def inh_tau(self):
        return self._inh_tau

    @inh_tau.setter
    def inh_tau(self, inh_tau):
        self._inh_tau = utility_calls.convert_param_to_numpy(
            inh_tau, self._n_neurons)


    def get_n_synapse_types(self):
        return 2 # EX and IH

    def get_synapse_id_by_target(self, target):

        if target == "excitatory":
            return 0
        elif target == "inhibitory":
            return 1
        return None

    def get_synapse_targets(self):
        return "excitatory",  "inhibitory"

    def get_n_synapse_type_parameters(self):
        return  12

    @inject_items({"machine_time_step": "MachineTimeStep"})
    def get_synapse_type_parameters(self, machine_time_step):
        e_a_decay, e_a_init = get_exponential_decay_and_init(
            self._exc_a_tau, machine_time_step)
        e_b_decay, e_b_init = get_exponential_decay_and_init(
            self._exc_b_tau, machine_time_step)
        i_decay, i_init = get_exponential_decay_and_init(
            self._inh_tau, machine_time_step)

        print "ex_a: decay = {}, init: {}".format(e_a_decay/float(pow(2, 32)), e_a_init/float(pow(2, 32)))
        print "ex_b: decay = {}, init: {}".format(e_b_decay/float(pow(2, 32)), e_b_init/float(pow(2, 32)))
        print "inh: decay = {}, init: {}".format(i_decay/float(pow(2, 32)), i_init/float(pow(2, 32)))

        return [
            NeuronParameter(self._exc_response, _DIFF_EXP_TYPES.E_RESPONSE.data_type),

            NeuronParameter(self._exc_a_response, _DIFF_EXP_TYPES.E_A_RESPONSE.data_type),
            NeuronParameter(self._exc_a_A, _DIFF_EXP_TYPES.E_A_A.data_type),
            NeuronParameter(e_a_decay, _DIFF_EXP_TYPES.E_A_DECAY.data_type),
            NeuronParameter(e_a_init, _DIFF_EXP_TYPES.E_A_INIT.data_type),

            NeuronParameter(self._exc_b_response, _DIFF_EXP_TYPES.E_B_RESPONSE.data_type),
            NeuronParameter(self._exc_b_B, _DIFF_EXP_TYPES.E_B_B.data_type),
            NeuronParameter(e_b_decay, _DIFF_EXP_TYPES.E_B_DECAY.data_type),
            NeuronParameter(e_b_init, _DIFF_EXP_TYPES.E_B_INIT.data_type),

            NeuronParameter(self._inh_response, _DIFF_EXP_TYPES.I_RESPONSE.data_type),
            NeuronParameter(i_decay, _DIFF_EXP_TYPES.I_DECAY.data_type),
            NeuronParameter(i_init, _DIFF_EXP_TYPES.I_INIT.data_type),
        ]

    def get_synapse_type_parameter_types(self):

        # TODO: update to return the parameter types
        return [item.data_type for item in DataType]

    def get_n_cpu_cycles_per_neuron(self):
        # a guess
        return 100
