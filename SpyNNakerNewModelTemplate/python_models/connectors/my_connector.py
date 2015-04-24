from spynnaker.pyNN.models.neural_projections.connectors.abstract_connector \
    import AbstractConnector
from spynnaker.pyNN.models.neural_properties.synaptic_list import SynapticList
from spynnaker.pyNN.models.neural_properties.synapse_row_info \
    import SynapseRowInfo
from spynnaker.pyNN.models.neural_properties.randomDistributions \
    import generate_parameter_array
import numpy


class MyConnector(AbstractConnector):
    """
    Connects two vertices with some thing

    """
    def __init__(self, weights=0.0, delays=1, allow_self_connections=True
                 # TODO: Add your parameters here
                 ):
        """
        Creates a new MyConnector
        """
        self._weights = weights
        self._delays = delays
        self._allow_self_connections = allow_self_connections

        # TODO: Store any additional parameters

    def generate_synapse_list(
            self, presynaptic_population, postsynaptic_population, delay_scale,
            weight_scale, synapse_type):
        """
        creates the matrix which says which neurons in the pre vertex connect\
        to neurons in the post vertex.

        :param presynaptic_population:  the population at the start of the\
                    projection
        :param postsynaptic_population: the population at the end of the\
                    projection
        :param delay_scale: Scale factor to be multiplied by all generated\
                    delays
        :param weight_scale: Scale factor to be multiplied by all generated\
                    weights
        :param synapse_type: The type of the synapse
        :return: returns a synaptic list of SynapseRowInfo
        """

        prevertex = presynaptic_population._get_vertex
        postvertex = postsynaptic_population._get_vertex

        connection_list = list()
        # TODO: do calculation for which neurons connect to which here!

        return SynapticList(connection_list)
