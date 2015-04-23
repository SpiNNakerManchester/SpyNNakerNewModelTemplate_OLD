#ifndef _TIMING_MY_IMPL_H_
#define _TIMING_MY_IMPL_H_

//---------------------------------------
// Typedefines
//---------------------------------------
// Define what will be stored in the post trace information
typedef int16_t post_trace_t;

// Define what will be stored in the pre trace information
typedef int16_t pre_trace_t;

// This must be included here after the above have been defined
#include "timing.h"

// Choose a weight dependence type here
#include "../weight_dependence/weight_one_term.h"
//#include "../weight_dependence/weight_two_term.h"

// Include debug header for log_info etc
#include <debug.h>

// Include generic plasticity maths functions
#include "../../common/maths.h"
#include "../../common/stdp_typedefs.h"


static inline post_trace_t timing_get_initial_post_trace() {

    // Return the initial value of the post trace (depends on the type)
    return INITIAL_VALUE;
}

static inline post_trace_t timing_add_post_spike(
        uint32_t time, uint32_t last_time, post_trace_t last_trace) {

    // Return a new post-trace following a post spike
    return NEW_POST_TRACE;
}

//---------------------------------------
static inline pre_trace_t timing_add_pre_spike(
        uint32_t time, uint32_t last_time, pre_trace_t last_trace) {

    // Return a new pre-trace following a pre spike
    return NEW_PRE_TRACE;
}

//---------------------------------------
static inline update_state_t timing_apply_pre_spike(
        uint32_t time, pre_trace_t trace, uint32_t last_pre_time,
        pre_trace_t last_pre_trace, uint32_t last_post_time,
        post_trace_t last_post_trace, update_state_t previous_state) {

    // Apply some depression depending on the pre-spike rule

    // Return the updated state information
    return UPDATED_STATE;
}

//---------------------------------------
static inline update_state_t timing_apply_post_spike(
        uint32_t time, post_trace_t trace, uint32_t last_pre_time,
        pre_trace_t last_pre_trace, uint32_t last_post_time,
        post_trace_t last_post_trace, update_state_t previous_state) {

    // Apply some potentiation depending on the post-spike rule

    // Return the updated state information
    return UPDATED_STATE;
}

#endif // _TIMING_MY_IMPL_H_
