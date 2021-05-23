
Implementing Python C Extension on Kivy Android
================================================

This section will give an basic implementation of python C extension on kivy android using recipe for buildozer / p4a

Template for building the Android application

https://github.com/VICTORVICKIE/Kivy_Python_C_Extension_Demo

Kivy app
----------
Create a project folder (Kivy_Python_C_Extension_Demo)

Create a basic kivy app (main.py)

.. code-block:: python 
  :emphasize-lines: 4,9

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

