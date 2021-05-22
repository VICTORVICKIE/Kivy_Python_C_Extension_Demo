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