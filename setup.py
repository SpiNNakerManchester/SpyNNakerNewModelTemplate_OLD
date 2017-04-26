from setuptools import setup

setup(
    name="ONeuron",
    version="0",
    packages=['python_models',],
    package_data={'python_models.model_binaries': ['*.aplx']},
    install_requires=['SpyNNaker >= 3.0.0, < 4.0.0']
)

setup(
    name="my_model_curr_exp",
    version="0",
    packages=['python_models',],
    package_data={'python_models.model_binaries': ['*.aplx']},
    install_requires=['SpyNNaker >= 3.0.0, < 4.0.0']
)