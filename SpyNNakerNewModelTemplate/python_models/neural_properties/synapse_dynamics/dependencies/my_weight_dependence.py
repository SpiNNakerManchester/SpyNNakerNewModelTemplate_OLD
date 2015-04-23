"""
MyWeightDependence
"""

from data_specification.enums.data_type import DataType
from spynnaker.pyNN.models.neural_properties.synapse_dynamics.abstract_rules.\
    abstract_weight_dependency import AbstractWeightDependency


class MyWeightDependence(AbstractWeightDependency):

    # noinspection PyPep8Naming
    def __init__(self, w_min=0.0, w_max=1.0, A_plus=0.01, A_minus=0.01,
                 A3_plus=None, A3_minus=None
                 # add params here
                 ):
        AbstractWeightDependency.__init__(self, w_min=w_min, w_max=w_max,
                                          A_plus=A_plus, A_minus=A_minus,
                                          A3_plus=A3_plus, A3_minus=A3_minus)

    def is_weight_dependance_rule_part(self):
        """
        helper method for isinstance
        :return:
        """
        return True

    def __eq__(self, other):
        """
        check that two MyWeightDependence are equal to each other
        :param other:
        :return:
        """
        if (other is None) or (not isinstance(other, MyWeightDependence)):
            return False
        return ((self._w_min == other.w_min) and
                (self._w_max == other.w_max) and
                (self._A_plus == other.A_plus) and
                (self._A_minus == other.A_minus) and
                (self._A3_plus == other.A3_plus) and
                (self._A3_minus == other.A3_minus))

    def get_params_size_bytes(self, num_synapse_types, num_terms):
        """
        returns ?????
        :param num_synapse_types: how many different types of synapsies will
         be adjusted
        :param num_terms: ??????/
        :return:
        """
        return # a int here

    def write_plastic_params(self, spec, machine_time_step, weight_scales,
                             global_weight_scale, num_terms):
        # write your palastic params to dsg
        pass

    @property
    def vertex_executable_suffix(self):
        """
        human readable suffix for this pastic part
        :return:
        """
        return "additive"
