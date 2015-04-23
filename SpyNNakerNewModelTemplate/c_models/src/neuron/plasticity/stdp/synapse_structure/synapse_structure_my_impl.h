/* Use this file to create your own plastic synapse information.  This can
 * be anything that you want to use to calculate new synaptic data.  The
 * template below is set up for simple weights, but you can add other things
 * here.
 */

#ifndef _SYNAPSE_STRUCUTRE_MY_IMPL_H_
#define _SYNAPSE_STRUCUTRE_MY_IMPL_H_

//---------------------------------------
// Structures
//---------------------------------------
// Structure for plastic synapse information
typedef struct plastic_synapse_t {
    weight_t weight;

    // Add any additional values here
} plastic_synapse_t;

// Structure for synapse state update
typedef struct update_state_t {
    weight_state_t weight_state;

    // Add any additional values here
} update_state_t;

// Structure for the final state after update
typedef plastic_synapse_t final_state_t;

// This must be included after the above definitions
#include "neuron/plasticity/stdp/synapse_structure/synapse_structure.h"

static inline update_state_t synapse_structure_get_update_state(
        plastic_synapse_t synaptic_word, index_t synapse_type) {

    // Convert your plastic_synapse_t into a update_state_t
    update_state_t update_state;
    update_state.weight_state = weight_get_initial(synaptic_word.weight,
                                                   synapse_type);

    // Add any additional variables from the plastic synapse to the update
    // state

    return update_state;
}

//---------------------------------------
static inline final_state_t synapse_structure_get_final_state(
        update_state_t state) {

    // Convert your update_state into a final state to be written back

    weight_t weight = weight_get_final(state.weight_state);
    return (final_state_t) {
        .weight = weight,
    };
}

//---------------------------------------
static inline weight_t synapse_structure_get_final_weight(
        final_state_t final_state) {

    // Get the final weight from the final state

    return final_state.weight;
}

//---------------------------------------
static inline plastic_synapse_t synapse_structure_get_final_synaptic_word(
        final_state_t final_state) {

    // Get the final plastic synapse from the final state

    return final_state;
}

#endif _SYNAPSE_STRUCUTRE_MY_IMPL_H_
