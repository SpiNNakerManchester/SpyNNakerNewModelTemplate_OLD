#ifndef _NEURON_MODEL_MY_IMPL_H_
#define _NEURON_MODEL_MY_IMPL_H_

#include <neuron/models/neuron_model.h>

typedef struct neuron_t {

    // TODO: Parameters - make sure these match with the python code!

    // Variable-state parameters e.g. membrane voltage
    REAL V;

    // offset current [nA]
    REAL I_offset;

    // Put anything else you want to store per neuron
    REAL my_parameter;

} neuron_t;

// function that converts the input into the real value to be used by the
// neuron - this can be used for scaling for example
// (as is done for conductance)
inline input_t neuron_model_convert_input(input_t input) {
    return input;
}

#endif   // _NEURON_MODEL_MY_IMPL_H_
