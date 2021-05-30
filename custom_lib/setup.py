from setuptools import find_packages, Extension, setup


setup(

    name = 'custom_lib',
    
    version = '0.1',

    description = 'This package contains some sample hello world C code',

    author = 'VIGNESH KUMAR S',
    
    author_email = 's.vickie14@gmail.com',

    url = 'https://github.com/VICTORVICKIE/Kivy_Python_C_Extension_Demo',

    packages = find_packages(),

    ext_package = 'custom_lib',
    
    ext_modules = [Extension('custom_module',['custom_lib/custom_module.c'])],

    entry_points = {'console_scripts': ['custom-lib-cli = custom_lib.custom_module:custom_hello', ], },

)