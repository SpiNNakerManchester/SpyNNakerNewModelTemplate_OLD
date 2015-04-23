"""
my time dependance
"""

from spynnaker.pyNN.models.neural_properties.synapse_dynamics.abstract_rules.\
    abstract_time_dependency import AbstractTimeDependency
from spynnaker.pyNN.models.neural_properties.synapse_dynamics.\
    plastic_weight_synapse_row_io import PlasticWeightSynapseRowIo
from spynnaker.pyNN.models.neural_properties.synapse_dynamics\
    import plasticity_helpers

import logging
logger = logging.getLogger(__name__)


class MyTimeDependency(AbstractTimeDependency):
    """
    my time dependance
    """

    def __init__(self,  # add paramteres here
                 ):
        AbstractTimeDependency.__init__(self)

    def __eq__(self, other):
        if (other is None) or (not isinstance(other, MyTimeDependency)):
            return False
        return # add functions here for telling if two MyTimeDependency are equal

    def create_synapse_row_io(
            self, synaptic_row_header_words, dendritic_delay_fraction):
        """

        :param synaptic_row_header_words:
        :param dendritic_delay_fraction:
        :return:
        """
        return PlasticWeightSynapseRowIo(
            synaptic_row_header_words, dendritic_delay_fraction)

    def get_params_size_bytes(self):
        """
        returns how many bytes
        :return:
        """
        return # return a number here

    def is_time_dependance_rule_part(self):
        """
        helper emthod for is instance
        :return:
        """
        return True

    def write_plastic_params(self, spec, machine_time_step, weight_scales,
                             global_weight_scale):
        """

        :param spec:
        :param machine_time_step:
        :param weight_scales:
        :param global_weight_scale:
        :return:
        """
        # write the plastic params into the dsg spec.
        pass

    @property
    def num_terms(self):
        """
        returns the number of terms (forced by abstract time dependance)
        :return:
        """
        return 1

    @property
    def vertex_executable_suffix(self):
        """
        a human readable form of this rule
        :return:
        """
        return "nearest_pair" if self._nearest else "pair"

    @property
    def pre_trace_size_bytes(self):
        """
        no diea
        :return:
        """
        # Pair rule requires no pre-synaptic trace when only the nearest
        # Neighbours are considered and, a single 16-bit R1 trace
        return 0 if self._nearest else 2

