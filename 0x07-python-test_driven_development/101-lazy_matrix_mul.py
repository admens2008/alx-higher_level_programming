#!/usr/bin/python3
""" Numpy Module
"""
import numpy

'''
File_name: 101-lazy_matrix_mul.py
Project: 0x07-python-test_driven_development
'''


def lazy_matrix_mul(m_a, m_b):
    """
    # Write a function that multiplies 2 matrices by using the module NumPy...
    # Test cases should be the same as 100-matrix_mul but with....
    # new exception type/message
    # VARIABLE(" "):
    # Lazy_Numpy: Lazy matrix multiplication
    # Return: Always 0. (Success).
    """
    return numpy.matmul(m_a, m_b)
