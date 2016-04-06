APP = $(notdir $(CURDIR))
BUILD_DIR = build/

NEURON_MODEL = $(SOURCE_DIRS)/neuron/neuron_components/models/neuron_model_lif_impl.o
NEURON_MODEL_H = $(SOURCE_DIRS)/neuron/neuron_components/models/neuron_model_lif_impl.h
INPUT_TYPE_H = $(SOURCE_DIRS)/neuron/neuron_components/input_types/input_type_current.h
THRESHOLD_TYPE_H = $(SOURCE_DIRS)/neuron/neuron_components/threshold_types/threshold_type_static.h
SYNAPSE_TYPE_H = $(SOURCE_DIRS)/neuron/neuron_components/synapse_types/synapse_types_exponential_impl.h
SYNAPSE_DYNAMICS = $(SOURCE_DIRS)/neuron/neuron_components/plasticity/stdp/synapse_dynamics_static_impl.o

include ../Makefile.common
