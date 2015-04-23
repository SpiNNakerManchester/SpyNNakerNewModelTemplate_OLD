/*! \file
 * \brief implementation of synapse_types.h for Exponential shaping
*
* \details This is used to give a simple exponential decay to synapses.
*
* If we have combined excitatory/inhibitory synapses it will be
* because both excitatory and inhibitory synaptic time-constants
* (and thus propogators) are identical.
*/


#ifndef _SYNAPSE_TYPES_MY_IMPL_H_
#define _SYNAPSE_TYPES_MY_IMPL_H_

// This is currently used for decaying the neuron input
#include <neuron/decay.h>

#include <debug.h>

// Determines the number of bits required by the synapse type in the synapse
// row data structure (i.e. enough bits to represent all desired synapse types)
// e.g. 1 bit for 2 possible types such as excitatory and inhibitory
#define SYNAPSE_TYPE_BITS 1

// Determines the number of synapse types required (e.g. 2 for excitatory and
// inhibitory)
#define SYNAPSE_TYPE_COUNT 2

// Defines the parameters required to compute the synapse shape
typedef struct synapse_param_t {
    decay_t neuron_synapse_decay;
    decay_t neuron_synapse_init;
} synapse_param_t;

// Include this here after defining the above items
#include "synapse_types.h"

//! \brief Shapes the values input into the neurons
//! \param[in-out] input_buffers the pointer to the input buffers to be shaped
//! \param[in] neuron_index the index of the neuron for which the value is to
//                          shaped
//! \param[in] parameters the synapse parameters passed in
//! \return nothing
static inline void synapse_types_shape_input(
        input_t *input_buffers, index_t neuron_index,
        synapse_param_t** parameters) {

    // This is the index of the input to the first synapse (index 0)
    uint32_t first_synapse_index = synapse_types_get_input_buffer_index(
        0, neuron_index);
    input_buffers[first_synapse_index] = NEW_VALUE;
}

//! \brief Adds the initial value to an input buffer for this shaping.  Allows
//         the input to be scaled before being added.
//! \param[in-out] input_buffers the pointer to the input buffers
//! \param[in] synapse_type_index the index of the synapse type to add the
//                                value to
//! \param[in] neuron_index the index of the neuron to add the value to
//! \param[in] parameters the synapse parameters passed in
//! \param[in] input the input to be added
//! \return None
static inline void synapse_types_add_neuron_input(
        input_t *input_buffers, index_t synapse_type_index,
        index_t neuron_index, synapse_param_t** parameters, input_t input) {

    uint32_t input_index = synapse_types_get_input_buffer_index(
        synapse_type, neuron_index);
    input_buffers[input_index] += input;
}

//! \brief Gets the excitatory input for a given neuron
//! \param[in] input_buffers the pointer to the input buffers
//! \param[in] neuron_index the index of the neuron to be updated
//! \return the excitatory input value
static inline input_t synapse_types_get_excitatory_input(
        input_t *input_buffers, index_t neuron_index) {

    // This gets the first synapse index - depends if this represents
    // excitatory input in your model
    uint32_t ex_synapse_index = synapse_types_get_input_buffer_index(
        0, neuron_index);
    return input_buffers[ex_synapse_index];
}

//! \brief Gets the inhibitory input for a given neuron
//! \param[in] input_buffers the pointer to the input buffers
//! \param[in] neuron_index the index of the neuron to be updated
//! \return the inhibitory input value
static inline input_t synapse_types_get_inhibitory_input(
        input_t *input_buffers, index_t neuron_index) {

    // This gets the second synapse index - depends if this represents
    // inhibitory input in your model
    uint32_t in_synapse_index = synapse_types_get_input_buffer_index(
        1, neuron_index);
    return input_buffers[in_synapse_index];
}

//! \brief returns a human readable character for the type of synapse, for
//         debug purposes
//! examples would be X = excitatory types, I = inhibitory types etc etc.
//! \param[in] synapse_type_index the synapse type index
//! \return a human readable character representing the synapse type.
static inline const char *synapse_types_get_type_char(
        index_t synapse_type_index) {
    if (synapse_type_index == 0) {
        return "X";
    } else if (synapse_type_index == 1)  {
        return "I";
    } else {
        log_debug("did not recognise synapse type %i", synapse_type_index);
        return "?";
    }
}

//! \brief prints the input for a neuron id for debug purposes
//! \param[in] input_buffers the pointer to the input buffers
//! \param[in] neuron_index the id of the neuron to print the input for
//! \return Nothing
static inline void synapse_types_print_input(
        input_t *input_buffers, index_t neuron_index) {

    uint32_t ex_synapse_index = synapse_types_get_input_buffer_index(
            0, neuron_index);
    uint32_t in_synapse_index = synapse_types_get_input_buffer_index(
            1, neuron_index);
    io_printf(
        IO_BUF, "%12.6k - %12.6k",
        input_buffers[ex_synapse_index], input_buffers[in_synapse_index]);
}

#endif  // _SYNAPSE_TYPES_MY_IMPL_H_
