#!/usr/bin/python3

"""
This program demonstrates the addition of two numbers.

Example:
    python add.py
"""

def add(a, b):
    """
    Adds two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

