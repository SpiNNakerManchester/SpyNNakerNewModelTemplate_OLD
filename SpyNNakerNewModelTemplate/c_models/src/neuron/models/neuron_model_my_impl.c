#include "neuron_model_my_impl.h"

#include <debug.h>

// machine timestep in msecs
static REAL machine_timestep = REAL_CONST(1.0);

void neuron_model_set_machine_timestep(timer_t microsecs) {

    // Store the machine timestep
    const double time_step_multiplier = 0.00100;
    machine_timestep = (REAL) (microsecs * time_step_multiplier);
}

bool neuron_model_state_update(input_t exc_input, input_t inh_input,
                               input_t external_bias, neuron_pointer_t neuron) {

    // This takes the input and generates an input value, assumed to be a
    // current.  If a conductance is expected as input, you will need to
    // do something different here!
    input_t input_this_timestep = exc_input - inh_input
                                  + external_bias + neuron->I_offset;


    // TODO: Solve your equation here
    neuron->V += input_this_timestep;

    // Return true if a spike is generated, or false otherwise
    return false;
}

state_t neuron_model_get_membrane_voltage(neuron_pointer_t neuron) {

    // TODO: Get the state value representing the membrane voltage
    return neuron->V;
}

void neuron_model_print(restrict neuron_pointer_t neuron) {

    // TODO: Printout of neuron definition and state variables
}
