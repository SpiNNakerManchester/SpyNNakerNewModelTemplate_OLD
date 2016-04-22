
from data_specification.enums.data_type import DataType
from spynnaker.pyNN.models.neuron.plasticity.stdp.weight_dependence\
    .abstract_weight_dependence import AbstractWeightDependence


class MyWeightDependence(AbstractWeightDependence):
    """
    my weight dependence
    """

    # noinspection PyPep8Naming
    def __init__(
            self,

            # TODO: Add any parameters
            w_min=0.0, w_max=1.0, A_plus=0.01, A_minus=0.01,
            A3_plus=None, A3_minus=None):

        AbstractWeightDependence.__init__(self)

        # TODO: Store any parameters
        self._w_min = w_min
        self._w_max = w_max
        self._A_plus = A_plus
        self._A_minus = A_minus
        self._A3_plus = A3_plus
        self._A3_minus = A3_minus

    def is_same_as(self, weight_dependence):
        """
        method to verify if 2 weight dependence's are the same
        :param weight_dependence: other weight dependence
        :return: true or false
        """
        if not isinstance(weight_dependence, MyWeightDependence):
            return False
        return (  # TODO: update to check important parameters
            (self._w_min == weight_dependence._w_min) and
            (self._w_max == weight_dependence._w_max) and
            (self._A_plus == weight_dependence._A_plus) and
            (self._A_minus == weight_dependence._A_minus) and
            (self._A3_plus == weight_dependence._A3_plus) and
            (self._A3_minus == weight_dependence._A3_minus))

    @property
    def vertex_executable_suffix(self):
        # TODO: add the text that a c compiled binary will have to represent it contains this weight dependence.
        return "additive"

    def get_parameters_sdram_usage_in_bytes(
            self, n_synapse_types, n_weight_terms):
        """ Get the amount of SDRAM used by the parameters of this rule
        """

        # TODO: update accordingly
        if n_weight_terms == 1:
            return (4 * 4) * n_synapse_types
        elif n_weight_terms == 2:
            return (6 * 4) * n_synapse_types
        else:
            raise NotImplementedError(
                "Additive weight dependence only supports one or two terms")

    def write_parameters(
            self, spec, machine_time_step, weight_scales, n_weight_terms):
        """ Write the parameters of the rule to the spec
        """

        # TODO: update accordingly
        # Loop through each synapse type's weight scale
        for w in weight_scales:

            # Scale the weights
            spec.write_value(
                data=int(round(self._w_min * w)), data_type=DataType.INT32)
            spec.write_value(
                data=int(round(self._w_max * w)), data_type=DataType.INT32)

            # Based on http://data.andrewdavison.info/docs/PyNN/_modules/pyNN
            #                   /standardmodels/synapses.html
            # Pre-multiply A+ and A- by Wmax
            spec.write_value(
                data=int(round(self._A_plus * self._w_max * w)),
                data_type=DataType.INT32)
            spec.write_value(
                data=int(round(self._A_minus * self._w_max * w)),
                data_type=DataType.INT32)

            # If triplet term is required, write A3+ and A3-, also multiplied
            # by Wmax
            if n_weight_terms == 2:
                spec.write_value(
                    data=int(round(self._A3_plus * self._w_max * w)),
                    data_type=DataType.INT32)
                spec.write_value(
                    data=int(round(self._A3_minus * self._w_max * w)),
                    data_type=DataType.INT32)
            elif n_weight_terms != 1:
                raise NotImplementedError(
                    "Additive weight dependence only supports one or two"
                    " terms")

    @property
    def weight_maximum(self):
        """ The maximum weight that will ever be set in a synapse as a result\
            of this rule
        """

        # TODO: update accordingly
        return self._w_max
