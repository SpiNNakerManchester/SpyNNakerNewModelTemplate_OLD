APP = $(notdir $(CURDIR))
BUILD_DIR = build/

NEURON_MODEL = $(SOURCE_DIRS)/neuron/neuron_components/models/neuron_model_lif_impl.o
NEURON_MODEL_H = $(SOURCE_DIRS)/neuron/neuron_components/models/neuron_model_lif_impl.h
INPUT_TYPE_H = $(SOURCE_DIRS)/neuron/neuron_components/input_types/input_type_current.h
THRESHOLD_TYPE_H = $(SOURCE_DIRS)/neuron/neuron_components/threshold_types/threshold_type_static.h
SYNAPSE_TYPE_H = $(SOURCE_DIRS)/neuron/neuron_components/synapse_types/synapse_types_exponential_impl.h
SYNAPSE_DYNAMICS = $(SOURCE_DIRS)/neuron/neuron_components/plasticity/stdp/synapse_dynamics_stdp_mad_impl.o
TIMING_DEPENDENCE = $(SOURCE_DIRS)/neuron/neuron_components/plasticity/stdp/timing_dependence/timing_nearest_pair_impl.o
TIMING_DEPENDENCE_H = $(SOURCE_DIRS)/neuron/neuron_components/plasticity/stdp/timing_dependence/timing_nearest_pair_impl.h
WEIGHT_DEPENDENCE = $(SOURCE_DIRS)/neuron/neuron_components/plasticity/stdp/weight_dependence/weight_additive_one_term_impl.o
WEIGHT_DEPENDENCE_H = $(SOURCE_DIRS)/neuron/neuron_components/plasticity/stdp/weight_dependence/weight_additive_one_term_impl.h

include ../Makefile.common
