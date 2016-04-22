#ifndef _THRESHOLD_TYPE_STATIC_H_
#define _THRESHOLD_TYPE_STATIC_H_

#include <neuron/threshold_types/threshold_type.h>

typedef struct threshold_type_t {

    // TODO: Add any additional parameters here

    REAL threshold_value;

    REAL my_param;

} threshold_type_t;

static inline bool threshold_type_is_above_threshold(state_t value,
                        threshold_type_pointer_t threshold_type) {
    REAL test_value = value * threshold_type->my_param;
    return REAL_COMPARE(test_value, >=, threshold_type->threshold_value);
}

#endif // _THRESHOLD_TYPE_STATIC_H_
