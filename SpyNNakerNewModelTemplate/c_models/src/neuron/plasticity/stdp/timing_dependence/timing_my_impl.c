#include "timing_pair_impl.h"

// Set up any global variables required here

//---------------------------------------
// Functions
//---------------------------------------
address_t timing_initialise(address_t address) {

    log_info("timing_initialise: starting");
    log_info("\tSTDP pair rule");

    // Initialise your global variables here

    log_info("timing_initialise: completed successfully");

    // Return the address *after* you have copied your variables i.e. the
    // address of the first byte following the data you have read above
    return address;
}
