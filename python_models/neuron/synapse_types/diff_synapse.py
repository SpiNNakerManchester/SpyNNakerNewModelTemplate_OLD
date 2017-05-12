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
    E_INPUT_BUFFER_VALUE = (1, DataType.S1615)
    E_A_DECAY = (2, DataType.UINT32)
    E_A_INIT = (3, DataType.UINT32)
    E_A_INIT_I = (4, DataType.S1615)
    E_B_DECAY = (5, DataType.UINT32)
    E_B_INIT = (6, DataType.UINT32)
    E_B_INIT_I = (7, DataType.S1615)
    I_DECAY = (8, DataType.UINT32)
    I_INIT = (9, DataType.UINT32)
    I_INIT_I = (10, DataType.S1615)

    def __new__(cls, value, data_type):
        obj = object.__new__(cls)
        obj._value_ = value
        obj._data_type = data_type
        return obj

    @property
    def data_type(self):
        return self._data_type


class DiffSynapseType(AbstractSynapseType):

    def __init__(self, n_neurons,
                exc_inp_buf_val,
                exc_A_tau,
                exc_A_init_i,
                exc_B_tau,
                exc_B_init_i,
                inh_tau,
                inh_init_i):

        AbstractSynapseType.__init__(self)
        self._n_neurons = n_neurons

        self._exc_inp_buf_val = utility_calls.convert_param_to_numpy(exc_inp_buf_val, n_neurons)

        self._exc_A_tau = utility_calls.convert_param_to_numpy(exc_A_tau, n_neurons)
        self._exc_A_init_i = utility_calls.convert_param_to_numpy(exc_A_init_i, n_neurons)

        self._exc_B_tau = utility_calls.convert_param_to_numpy(exc_B_tau, n_neurons)
        self._exc_B_init_i = utility_calls.convert_param_to_numpy(exc_B_init_i, n_neurons)

        self._inh_tau = utility_calls.convert_param_to_numpy(inh_tau, n_neurons)
        self._inh_init_i = utility_calls.convert_param_to_numpy(inh_init_i, n_neurons)


    @property
    def exc_inp_buf_val(self):
        return self._exc_inp_buf_val

    @exc_inp_buf_val.setter
    def exc_inp_buf_val(self, exc_inp_buf_val):
        self._exc_inp_buf_val = utility_calls.convert_param_to_numpy(
            exc_inp_buf_val, self._n_neurons)



    @property
    def exc_A_tau(self):
        return self._exc_A_tau

    @exc_A_tau.setter
    def exc_A_tau(self, exc_A_tau):
        self._exc_A_tau = utility_calls.convert_param_to_numpy(
            exc_A_tau, self._n_neurons)

    @property
    def exc_A_init_i(self):
        return self._exc_A_init_i

    @exc_A_init_i.setter
    def exc_A_init_i(self, exc_A_init_i):
        self._exc_A_init_i = utility_calls.convert_param_to_numpy(
            exc_A_init_i, self._n_neurons)

    @property
    def exc_B_tau(self):
        return self._exc_B_tau

    @exc_B_tau.setter
    def exc_B_tau(self, exc_B_tau):
        self._exc_B_tau = utility_calls.convert_param_to_numpy(
            exc_B_tau, self._n_neurons)

    @property
    def exc_B_init_i(self):
        return self._exc_B_init_i

    @exc_B_tau.setter
    def exc_B_tau(self, exc_B_init_i):
        self._exc_B_init_i = utility_calls.convert_param_to_numpy(
            exc_B_init_i, self._n_neurons)

    @property
    def inh_tau(self):
        return self._inh_tau

    @inh_tau.setter
    def inh_tau(self, inh_tau):
        self._inh_tau = utility_calls.convert_param_to_numpy(
            inh_tau, self._n_neurons)

    @property
    def inh_init_i(self):
        return self._inh_tau

    @inh_tau.setter
    def inh_init_i(self, inh_init_i):
        self._inh_init_i = utility_calls.convert_param_to_numpy(
            inh_init_i, self._n_neurons)


    def get_n_synapse_types(self):
        return 2 # EX and IH

    def get_synapse_id_by_target(self, target):

        # TODO: update the mapping from name to id
        if target == "excitatory":
            return 0
        #if target == "excitatory_A":
        #    return 1
        #elif target == "excitatory_B":
        #    return 2
        elif target == "inhibitory":
            return 1
        return None

    def get_synapse_targets(self):
        return "excitatory",  "inhibitory"

    def get_n_synapse_type_parameters(self):
        return 10

    @inject_items({"machine_time_step": "MachineTimeStep"})
    def get_synapse_type_parameters(self, machine_time_step):
        e_A_decay, e_A_init = get_exponential_decay_and_init(
            self._exc_A_tau, machine_time_step)
        e_B_decay, e_B_init = get_exponential_decay_and_init(
            self._exc_B_tau, machine_time_step)
        i_decay, i_init = get_exponential_decay_and_init(
            self._inh_tau, machine_time_step)

        print "ex_A: decay = {}, init: {}".format(e_A_decay/float(pow(2, 32)), e_A_init/float(pow(2, 32)))
        print "ex_B: decay = {}, init: {}".format(e_B_decay/float(pow(2, 32)), e_B_init/float(pow(2, 32)))
        print "inh: decay = {}, init: {}".format(i_decay/float(pow(2, 32)), i_init/float(pow(2, 32)))

        return [
            NeuronParameter(self._exc_inp_buf_val, _DIFF_EXP_TYPES.E_INPUT_BUFFER_VALUE.data_type),
            NeuronParameter(e_A_decay, _DIFF_EXP_TYPES.E_A_DECAY.data_type),
            NeuronParameter(e_A_init, _DIFF_EXP_TYPES.E_A_INIT.data_type),
            NeuronParameter(self._exc_A_init_i, _DIFF_EXP_TYPES.E_A_INIT_I.data_type),
            NeuronParameter(e_B_decay, _DIFF_EXP_TYPES.E_B_DECAY.data_type),
            NeuronParameter(e_B_init, _DIFF_EXP_TYPES.E_B_INIT.data_type),
            NeuronParameter(self._exc_B_init_i, _DIFF_EXP_TYPES.E_B_INIT_I.data_type),
            NeuronParameter(i_decay, _DIFF_EXP_TYPES.I_DECAY.data_type),
            NeuronParameter(i_init, _DIFF_EXP_TYPES.I_INIT.data_type),
            NeuronParameter(self._inh_init_i, _DIFF_EXP_TYPES.I_INIT_I.data_type)
        ]

    def get_synapse_type_parameter_types(self):

        # TODO: update to return the parameter types
        return [item.data_type for item in DataType]

    def get_n_cpu_cycles_per_neuron(self):
        # a guess
        return 100
