/*! \file
 * \brief implementation of synapse_types.h for a synapse behaviour
 *  calculated as the difference between two exponential functions
 */

#ifndef _DIFF_SYNAPSE_H_
#define _DIFF_SYNAPSE_H_

#include <neuron/decay.h>
#include <debug.h>

//---------------------------------------
// Macros
//---------------------------------------
#define SYNAPSE_TYPE_BITS 1
#define SYNAPSE_TYPE_COUNT 2

//---------------------------------------
// Synapse parameters
//---------------------------------------
typedef struct synapse_param_t {
	input_t exc_response;
	decay_t exc_A_decay;
	decay_t exc_A_init;
	input_t exc_A_response;
	decay_t exc_B_decay;
	decay_t exc_B_init;
	input_t exc_B_response;
	decay_t inh_decay;
	decay_t inh_init;
	input_t inh_response;
} synapse_param_t;

#include <neuron/synapse_types/synapse_types.h>

//! human readable definition for the positions in the input regions for the
//! different synapse types.
typedef enum input_buffer_regions {
	EXCITATORY, INHIBITORY,
} input_buffer_regions;


static inline void synapse_types_shape_input(synapse_param_pointer_t parameter){
	//(input_t *input_buffers, index_t neuron_index, synapse_param_t* parameters) {
	parameter->exc_A_response =  decay_s1615(
			parameter->exc_A_response,
			parameter->exc_A_decay);
	parameter->exc_B_response = decay_s1615(
			parameter->exc_B_response,
			parameter->exc_B_decay);

	parameter->inh_response = decay_s1615(
			parameter->inh_response,
			parameter->inh_decay);

	//log_info("Decay A value: %11.4k, Decay B value: %11.4k", parameters[neuron_index].exc_B_decay, parameters[neuron_index].exc_A_decay);
	parameter->exc_response = parameter->exc_B_response - parameter->exc_A_response;


	/* log_info("shaping comb %11.4k, A %11.4k, B %11.4k", input_buffers[_ex_offset(neuron_index)], input_buffers[_ex_B_offset(
					neuron_index)], input_buffers[_ex_A_offset(neuron_index)] );
	*/
}

static inline void synapse_types_add_neuron_input(
		index_t synapse_type_index,
		synapse_param_pointer_t parameter,
        input_t input){

	if (synapse_type_index == EXCITATORY) {

		parameter->exc_A_response =  parameter->exc_A_response +
				decay_s1615(input,
				parameter->exc_A_init);


		parameter->exc_B_response = parameter->exc_B_response +
				decay_s1615(input,
				parameter->exc_B_init);



		//log_info("init A value: %11.4k, init B value: %11.4k", parameters[neuron_index].exc_B_init, parameters[neuron_index].exc_A_init);

		parameter->exc_response = parameter->exc_B_response - parameter->exc_A_response;


		//input_buffers[_ex_offset(neuron_index)]= input_buffers[_ex_B_offset(neuron_index)] - input_buffers[_ex_A_offset(neuron_index)];

	    /* log_info("add_neu comb %11.4k, A %11.4k, B %11.4k", input_buffers[_ex_offset(neuron_index)], input_buffers[_ex_B_offset(
				neuron_index)], input_buffers[_ex_A_offset(neuron_index)] );
		*/

	} else if (synapse_type_index == INHIBITORY) {
		parameter->inh_response = parameter->inh_response +
				decay_s1615(input,
				parameter->inh_init);
	}
}

/*
 This method is called by the neuron update: calculate difference between the
 two inputs: note that we do A-B
 */
static inline input_t synapse_types_get_excitatory_input(
		synapse_param_pointer_t parameter) {
	return parameter->exc_response;
}

static inline input_t synapse_types_get_inhibitory_input(
		synapse_param_pointer_t parameter) {
	return parameter->inh_response;
}

static inline const char *synapse_types_get_type_char(
		index_t synapse_type_index) {
	if (synapse_type_index == EXCITATORY) {
		return "X";
    /*
	} else if (synapse_type_index == EXCITATORY_A) {
		return "X_A";
	} else if (synapse_type_index == EXCITATORY_B) {
		return "X_B";
		*/
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
        parameter->exc_response,
        parameter->exc_A_response,
        parameter->exc_B_response,
        parameter->inh_response);
}

static inline void synapse_types_print_parameters(synapse_param_pointer_t parameter) {
    log_debug("-------------------------------------\n");
	log_debug("exc_response  = %11.4k\n", parameter->exc_response);
	log_debug("exc_A_decay  = %11.4k\n", parameter->exc_A_decay);
	log_debug("exc_A_init   = %11.4k\n", parameter->exc_A_init);
	log_debug("exc_A_response  = %11.4k\n", parameter->exc_A_response);
	log_debug("exc_B_decay = %11.4k\n", parameter->exc_B_decay);
	log_debug("exc_B_init  = %11.4k\n", parameter->exc_B_init);
	log_debug("exc_B_response  = %11.4k\n", parameter->exc_B_response);
	log_debug("inh_decay  = %11.4k\n", parameter->inh_decay);
	log_debug("inh_init   = %11.4k\n", parameter->inh_init);
	log_debug("inh_response  = %11.4k\n", parameter->inh_response);
}

#endif // _DIFF_SYNAPSE_H_

