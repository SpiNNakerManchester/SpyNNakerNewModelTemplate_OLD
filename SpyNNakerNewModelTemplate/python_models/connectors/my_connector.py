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
    def __init__(self, weights=0.0, delays=1, allow_self_connections=True):
        """
        Creates a new MyConnector
        """
        self._weights = weights
        self._delays = delays
        self._allow_self_connections = allow_self_connections

    def generate_synapse_list(
            self, presynaptic_population, postsynaptic_population, delay_scale,
            weight_scale, synapse_type):
        """
        creates the matrix which says which neurons in the pre vertex
         conenct to neurons in the post vertex.
        :param presynaptic_population:  the pre vertex of a edge
        :param postsynaptic_population: the post vertex of the edge
        :param delay_scale: fudge factor to deal with fix point stuff.
        Please multiple all your delays by this value.
        :param weight_scale: fudge factor to deal with fix point stuff.
        Please multiple all your weights by this value.
        :param synapse_type:
        The type of saynapsie this conenctor deals with
        (excititary or inhibitary etc).
        :return: returns a synpatic list.
        """

        prevertex = presynaptic_population._get_vertex
        postvertex = postsynaptic_population._get_vertex

        connection_list = list()
        # do calcualtion for which neurons connect to whcih here!

        return SynapticList(connection_list)
