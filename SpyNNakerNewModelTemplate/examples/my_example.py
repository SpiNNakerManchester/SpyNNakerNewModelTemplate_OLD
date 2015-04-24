import pyNN.spiNNaker as p
from python_models.neural_models.my_model_curr_exp import MyModelCurrExp
from python_models.neural_models.my_model_curr_my_synapse_type import MyModelCurrMySynapseType

p.setup(1.0)

my_model_pop = p.Population(
    1, MyModelCurrExp, {"my_parameter": 2.0}, label="my_model_pop")
my_model_my_synapse_type_pop = p.Population(
    1, MyModelCurrMySynapseType, {"my_parameter": 3.0},
    label="my_model_my_synapse_type_pop")

p.run(100)
