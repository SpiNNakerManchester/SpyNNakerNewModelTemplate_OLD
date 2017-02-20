import os

if os.environ.get('READTHEDOCS', None) != 'True':
    from spynnaker.pyNN.spinnaker import executable_finder
    from python_models import model_binaries

    # This adds the model binaries path to the paths searched by sPyNNaker
    executable_finder.add_path(os.path.dirname(model_binaries.__file__))
