# New Model Template
This project contains a template for creating a new neural model.  This file
documents the process which can be followed to update the template to then
generate a working neural model.

This is split in to two sections, depending on if you just want to modify the
differential equation of the core neuron, or if you also want to modify the
synapse shaping of the input.


## Core Neuron Differential Equation
This template is set up to allow you to create your own core model differential
equation, but use a provided synapse type (initially an exponentially decaying
synapse type).

The template files to be modified are:
* c_models/src/neuron/models/neuron_model_my_impl.h
* c_models/src/neuron/models/neuron_model_my_impl.c
* python_models/neural_models/my_model_curr_exp.py
