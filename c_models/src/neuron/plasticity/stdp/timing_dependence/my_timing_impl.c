#include "my_timing_impl.h"

// TODO: Set up any variables here
int32_t my_parameter;

//---------------------------------------
// Functions
//---------------------------------------
address_t timing_initialise(address_t address) {

    log_info("timing_initialise: starting");
    log_info("\tSTDP my timing rule");

    // TODO: copy parameters from memory
    my_parameter = (int32_t) address[0];

    log_info("timing_initialise: completed successfully");

    // TODO: Return the address after the last one read
    return &address[1];
}
