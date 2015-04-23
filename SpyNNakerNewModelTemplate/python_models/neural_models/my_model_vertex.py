"""
My model
"""
from spynnaker.pyNN.models.abstract_models.abstract_population_vertex import \
    AbstractPopulationVertex
from spynnaker.pyNN.utilities import constants
from spynnaker.pyNN.models.abstract_models.abstract_model_components.\
    abstract_exp_population_vertex import AbstractExponentialPopulationVertex
from spynnaker.pyNN.models.abstract_models.abstract_model_components.\
    abstract_integrate_and_fire_properties \
    import AbstractIntegrateAndFireProperties
from spynnaker.pyNN.models.neural_properties.neural_parameter \
    import NeuronParameter


from data_specification.enums.data_type import DataType


class MyModel(  # Inheirrit from your required components: such as
                # AbstractExponentialPopulationVertex,
                # AbstractIntegrateAndFireProperties,
                AbstractPopulationVertex):
    """
    MY MDOEL!
    """

    CORE_APP_IDENTIFIER = constants.MyModel  # edit this to be a unqiue number
                                             # for your model. some magic
                                             # numebrs live in spynnaker
                                             # constants. others in front
                                             # end common constants.
    _model_based_max_atoms_per_core = 256

    # noinspection PyPep8Naming
    def __init__(self, n_neurons, machine_time_step, timescale_factor,
                 spikes_per_second, ring_buffer_sigma, constraints=None,
                 label=None,  # add extra parameters that you need here
                 ):
        # Instantiate the parent classes here (such as shown below)
        AbstractPopulationVertex.__init__(
            self, n_neurons=n_neurons, n_params=10, label=label,
            binary="model_my.aplx",  # fill in this with the name of the c code binary
            constraints=constraints,
            max_atoms_per_core=MyModel._model_based_max_atoms_per_core,
            machine_time_step=machine_time_step,
            timescale_factor=timescale_factor,
            spikes_per_second=spikes_per_second,
            ring_buffer_sigma=ring_buffer_sigma)
        self._executable_constant = MyModel.CORE_APP_IDENTIFIER

    @property
    def model_name(self):
        """
        returns the name of this model in a human readable form
        :return:
        """
        return "MyModel"  # edit this to be the name of your model in a
                          # human readable form

    @staticmethod
    def set_model_max_atoms_per_core(new_value):
        """
        is a hard method needed for spynnaker to allow pynn
        scripsts to control the max atoms per core on a model scope.
        :param new_value: the new max atoms per core for this model
        :return:None
        """
        MyModel._model_based_max_atoms_per_core = new_value

    def get_cpu_usage_for_atoms(self, vertex_slice, graph):
        """
        returns how much cpu ticks this model will use to simulate the neuron
        slice from the partitionable vertex.
        :param vertex_slice: the slice of neurons from the partitionable
        vertex that a partitioned vertex is expected to simulate
        :param graph: the partitionable graph object.
        :return: a number of cpu cycles
        """
        return # the number of cpu cycles expected (can be a guess)

    def get_dtcm_usage_for_atoms(self, vertex_slice, graph):
        """
        returns how much dtcm ticks this model will use to simulate the neuron
        slice from the partitionable vertex.
        :param vertex_slice: the slice of neurons from the partitionable
        vertex that a partitioned vertex is expected to simulate
        :param graph: the partitionable graph object.
        :return: a number of dtcm cycles
        """
        return  # the number of dtcm cycles expected (can be a guess)

    def get_parameters(self):
        """
        Generates the parameters ina  lsit for the dsg writer.
        NEEDS TO BE IN THE SAME ORDER AS THE C CODE EXPECTS
        """
        # Get the parameters
        # each paramter is a NeuronParameter which takes a value and a DataType
        # object as its parameters ane xample is:

        # NeuronParameter(self._v_reset, DataType.S1615),
        return []

    def is_population_vertex(self):
        """
        helper method for is instance
        :return:
        """
        return True

    def is_recordable(self):
        """
        helper method for is instance
        :return:
        """
        return True
