"""
This module provides basic arithmetic functions for addition, subtraction, and multiplication using numpy.
"""
import numpy as np




def add(a, b):
    """
    Add two numbers using numpy.

    Parameters:
    a (float or int): The first number.
    b (float or int): The second number.

    Returns:
    float: The sum of the two numbers.
    """
    return np.add(a, b)

def subtract(a, b):
    """
    Subtract the second number from the first number using numpy.

    Parameters:
    a (float or int): The first number.
    b (float or int): The second number.

    Returns:
    float: The difference of the two numbers.
    """
    return np.subtract(a, b)

def multiply(a, b):
    """
    Multiply two numbers using numpy.

    Parameters:
    a (float or int): The first number.
    b (float or int): The second number.

    Returns:
    float: The product of the two numbers.
    """
    return np.multiply(a, b)