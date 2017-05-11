/*! \file
 * \brief implementation of synapse_types.h for a synapse behaviour calculated as the difference between two exponential functions - sometimes called an 'alpha' input?
 *
 */

#ifndef _DIFF_SYNAPSE_H_
#define _DIFF_SYNAPSE_H_

#include <neuron/decay.h>
#include <debug.h>

//---------------------------------------
// Macros
//---------------------------------------
#define SYNAPSE_TYPE_BITS 2
#define SYNAPSE_TYPE_COUNT 4

//---------------------------------------
// Synapse parameters
//---------------------------------------
typedef struct synapse_param_t {
	input_t exc_input_buffer_value;
	decay_t exc_A_decay;
	decay_t exc_A_init;
	input_t exc_A_input_buffer_value;
	decay_t exc_B_decay;
	decay_t exc_B_init;
	input_t exc_B_input_buffer_value;
	decay_t inh_decay;
	decay_t inh_init;
	input_t inh_input_buffer_value;
} synapse_param_t;

#include <neuron/synapse_types/synapse_types.h>

//! human readable definition for the positions in the input regions for the
//! different synapse types.
typedef enum input_buffer_regions {
	EXCITATORY, EXCITATORY_A, EXCITATORY_B, INHIBITORY,
} input_buffer_regions;

//---------------------------------------
// Synapse shaping inline implementation
//---------------------------------------


/*
// Define helper methods here to improve code readability below
// Offsets
static inline index_t _ex_offset(index_t neuron_index) {
	return synapse_types_get_input_buffer_index(EXCITATORY, neuron_index);
}

static inline index_t _ex_A_offset(index_t neuron_index) {
	return synapse_types_get_input_buffer_index(EXCITATORY_A, neuron_index);
}

static inline index_t _ex_B_offset(index_t neuron_index) {
	return synapse_types_get_input_buffer_index(EXCITATORY_B, neuron_index);
}

static inline index_t _in_offset(index_t neuron_index) {
	return synapse_types_get_input_buffer_index(INHIBITORY, neuron_index);
}

// Decays
static inline decay_t _ex_A_decay(synapse_param_t *parameters,
		index_t neuron_index) {
	return (parameters[neuron_index].exc_A_decay);
}

static inline decay_t _ex_B_decay(synapse_param_t *parameters,
		index_t neuron_index) {
	return (parameters[neuron_index].exc_B_decay);
}

static inline decay_t _in_decay(synapse_param_t *parameters,
		index_t neuron_index) {
	return (parameters[neuron_index].inh_decay);
}

// Required implementation methods
*/

static inline void synapse_types_shape_input(synapse_param_pointer_t parameter){
	//(input_t *input_buffers, index_t neuron_index, synapse_param_t* parameters) {
	parameter->exc_A_input_buffer_value =  decay_s1615(
			parameter->exc_A_input_buffer_value,
			parameter->exc_A_decay);
	parameter->exc_B_input_buffer_value = decay_s1615(
			parameter->exc_B_input_buffer_value,
			parameter->exc_B_decay);

	parameter->inh_input_buffer_value = decay_s1615(
			parameter->inh_input_buffer_value,
			parameter->inh_decay);

	//log_info("Decay A value: %11.4k, Decay B value: %11.4k", parameters[neuron_index].exc_B_decay, parameters[neuron_index].exc_A_decay);
	parameter->exc_input_buffer_value = parameter->exc_B_input_buffer_value - parameter->exc_A_input_buffer_value;


	/* log_info("shaping comb %11.4k, A %11.4k, B %11.4k", input_buffers[_ex_offset(neuron_index)], input_buffers[_ex_B_offset(
					neuron_index)], input_buffers[_ex_A_offset(neuron_index)] );
	*/
}

static inline void synapse_types_add_neuron_input(
		index_t synapse_type_index,
		synapse_param_pointer_t parameter,
        input_t input){

	if (synapse_type_index == EXCITATORY) {

		parameter->exc_A_input_buffer_value =  parameter->exc_A_input_buffer_value +
				decay_s1615(parameter->exc_A_input_buffer_value,
				parameter->exc_A_init);


		parameter->exc_B_input_buffer_value = parameter->exc_B_input_buffer_value +
				decay_s1615(parameter->exc_B_input_buffer_value,
				parameter->exc_B_init);



		//log_info("init A value: %11.4k, init B value: %11.4k", parameters[neuron_index].exc_B_init, parameters[neuron_index].exc_A_init);

		parameter->exc_input_buffer_value = parameter->exc_B_input_buffer_value - parameter->exc_A_input_buffer_value;


		//input_buffers[_ex_offset(neuron_index)]= input_buffers[_ex_B_offset(neuron_index)] - input_buffers[_ex_A_offset(neuron_index)];

	    /* log_info("add_neu comb %11.4k, A %11.4k, B %11.4k", input_buffers[_ex_offset(neuron_index)], input_buffers[_ex_B_offset(
				neuron_index)], input_buffers[_ex_A_offset(neuron_index)] );
		*/

	} else if (synapse_type_index == INHIBITORY) {
		parameter->inh_input_buffer_value = parameter->inh_input_buffer_value +
				decay_s1615(parameter->inh_input_buffer_value,
				parameter->inh_init);
	}
}

/*
 This method is called by the neuron update: calculate difference between the
 two inputs: note that we do A-B
 */
static inline input_t synapse_types_get_excitatory_input(
		synapse_param_pointer_t parameter) {
	return parameter->exc_input_buffer_value;
}

static inline input_t synapse_types_get_inhibitory_input(
		synapse_param_pointer_t parameter) {
	return parameter->inh_input_buffer_value;
}

static inline const char *synapse_types_get_type_char(
		index_t synapse_type_index) {
	if (synapse_type_index == EXCITATORY) {
		return "X";
	} else if (synapse_type_index == EXCITATORY_A) {
		return "X_A";
	} else if (synapse_type_index == EXCITATORY_B) {
		return "X_B";
	} else if (synapse_type_index == INHIBITORY) {
		return "I";
	} else {
		log_debug("did not recognise synapse type %i", synapse_type_index);
		return "?";
	}
}

static inline void synapse_types_print_input(
        synapse_param_pointer_t parameter) {
    io_printf(
        IO_BUF, "%12.6k + %12.6k - %12.6k",
        parameter->exc_input_buffer_value,
        parameter->exc_A_input_buffer_value,
        parameter->exc_B_input_buffer_value,
        parameter->inh_input_buffer_value);
}

static inline void synapse_types_print_parameters(synapse_param_pointer_t parameter) {
	log_debug("exc_A_decay  = %11.4k\n", parameter->exc_A_decay);
	log_debug("exc_A_init   = %11.4k\n", parameter->exc_A_init);
	log_debug("exc_B_decay = %11.4k\n", parameter->exc_B_decay);
	log_debug("exc_B_init  = %11.4k\n", parameter->exc_B_init);
	log_debug("inh_decay  = %11.4k\n", parameter->inh_decay);
	log_debug("inh_init   = %11.4k\n", parameter->inh_init);
}

#endif // _DIFF_SYNAPSE_H_

