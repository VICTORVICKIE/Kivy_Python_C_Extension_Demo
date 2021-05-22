from setuptools import setup
from setuptools import Extension

setup(

    ext_package='custom_lib',
    ext_modules=[Extension('custom_module',['custom_lib/custom_module.c'])],

)