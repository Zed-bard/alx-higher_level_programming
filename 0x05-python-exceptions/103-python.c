#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - Prints information about a Python list object
 * @p: PyObject pointer to the Python list
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: PyObject pointer to the Python bytes
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	printf("[*] Python bytes info\n");
	printf("[*] Size of the Python Bytes = %ld\n", size);

	printf("first %ld bytes: ", size > 10 ? 10 : size);
	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: PyObject pointer to the Python float
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	printf("[*] Python float info\n");
	printf("[*] Value: %f\n", PyFloat_AsDouble(p));
}
