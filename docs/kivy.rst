
Python C Extension implementation on Kivy Android
==================================================

This section will give an basic implementation of python C extension on kivy android using recipe for buildozer / p4a

Template for building the Android application

https://github.com/VICTORVICKIE/Kivy_Python_C_Extension_Demo

Kivy app
----------
Create a project folder (Kivy_Python_C_Extension_Demo)

.. code-block:: console
   :caption: Directory Structure for Project

    Kivy_Python_C_Extension_Demo
    |
    ├── custom_lib
    |
    ├── python-for-android
    |
    └── main.py
    |
    └── buildozer.spec

Create a basic kivy app (main.py)

.. code-block:: python 
   :emphasize-lines: 4,9
   :caption: main.py

   from kivy.app import App
   from kivy.uix.label import Label

   from custom_lib import custom_module

   class PyCExtensionApp(App):

   def build(self):
       return Label(text=custom_module.custom_hello())


   if __name__ == '__main__':
       PyCExtensionApp().run()

This app just displays the text of string from the C Extension for demonstration.


C Extension 
--------------
In the project directory 

create a folder for the library (custom_lib)
this contains all the requirements for the C Extension

setup.py / setup.cfg

and src folder format package (custom_lib, This is different from previous one!)

In the src folder we need a __init__.py for package and a module file (Here C Extension)

And the structure should look similar to this

.. code-block:: console
   :caption: Directory Structure for Library

    custom_lib
    |
    ├── setup.cfg
    |
    ├── setup.py
    |
    └── custom_lib
    	|
        ├── custom_module.c
        |
        └── __init__.py


In custom_module.c

.. code-block:: C
  :emphasize-lines: 3-5
  :caption: custom_module.c

  #include <Python.h>

  static PyObject* custom_hello(PyObject* self){
      return PyUnicode_FromString("Hello from Custom Lib");
  }

  static struct PyModuleDef methods[] = {

      {"custom_hello", (PyCFunction)custom_hello, METH_NOARGS},
      {NULL, NULL}
  };

  static struct PyModuleDef module = {
      PyModuleDef_HEAD_INIT,
      "custom_module",
      NULL,
      -1,
      methods
  };

  PyMODINIT_FUNC PyInit_custom_module(void) {
      return PyModule_Create(&module);
  }

Setuptools
------------------------------------------

.. raw:: html

   <p align="center"><iframe width="560" height="315" src="https://www.youtube.com/embed/GaWs-LenLYE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>

.. code-block:: python
   :caption: setup.py
   :emphasize-lines: 5,17-23

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

Install the custom_lib by running the below command in directory where your setup.py exists

.. code-block:: console

	❯ pip install .

.. tip::

   The output of the above command should be something like this,

   ❯ Successfully built custom-lib

   ❯ Successfully installed custom-lib-0.1

Now check if the custom_lib works, with the cli command given in entry_points

.. code-block:: console

   ❯ custom-lib-cli

.. note::

   The output of the above command depends on your entry_points!

   here,

   ❯ Hello from Custom Lib

One final step to integrate the extension module with the application.

Recipe
------

https://python-for-android.readthedocs.io/en/latest/recipes/

Recipes are special scripts for compiling and installing different programs (including Python modules) into a p4a distribution. 
They are necessary to take care of compilation for any compiled components, as these must be compiled for Android with the correct architecture.

.. code-block:: console
   :caption: Directory Structure for Recipe

    python-for-android
    |
    └── recipe
    	  |
    	  └── custom_lib
          	  |
          	  └── __init__.py

.. code-block:: python 
   :caption: __init__.py

   from pythonforandroid.recipe import CompiledComponentsPythonRecipe

   class BillBookLibRecipe(CompiledComponentsPythonRecipe):

	   site_packages_name = 'custom_lib'
	   depends = ['setuptools']
   	   call_hostpython_via_targetpython = False

	
	   def should_build(self, arch):
		   return True

   recipe = BillBookLibRecipe()

Buildozer
----------

.. code-block:: console
   :caption: buildozer.spec

   # In requirements make sure to mention the C Extension Module
   requirements = python3,kivy,custom_lib

   # Specify the path for the setup.py / setup.cfg for local C Extension Module
   requirements.source.custom_lib = ./custom_lib/

   # Specify the path for Recipe for local C Extension Module
   p4a.local_recipes = ./python-for-android/recipe