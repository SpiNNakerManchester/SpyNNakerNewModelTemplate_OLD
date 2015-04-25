# This is the name of the application
# TODO: Ensure this matches the binary in the Python code
APP = my_model_curr_my_synapse_type

# This is the folder where things will be built (this will be created)
BUILD_DIR = build/

# This is the list of objects that will make up your neural model, as well as
# the synaptic plasticity type (or lack of if using static_impl)
# TODO: Add any extra objects to be compiled
MODEL_OBJS = $(EXTRA_SRC_DIR)/neuron/models/neuron_model_my_impl.o\
             $(SOURCE_DIRS)/neuron/plasticity/synapse_dynamics_static_impl.o
             
# This is the header of the neuron model, containing the definintion of
# neuron_t
# TODO: Ensure this matches your neuron model header name
NEURON_MODEL_H = $(EXTRA_SRC_DIR)/neuron/models/neuron_model_my_impl.h

# This is the header containing the synapse shaping type 
# (exponential in this case)
# TODO: Ensure that this is the desired shaping
SYNAPSE_TYPE_H = $(EXTRA_SRC_DIR)/neuron/synapse_types/synapse_types_my_impl.h

# This is the "MAGIC NUMBER" that should match the Python "CORE_APP_IDENTIFIER"
# TODO: Ensure that this matches the python CORE_APP_IDENTIFIER
APPLICATION_MAGIC_NUMBER = 0x12345679

include ../Makefile.common
