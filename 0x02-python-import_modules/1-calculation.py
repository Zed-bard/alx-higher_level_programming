#!/usr/bin/python3
if __name__ == "__main__":
    """Importing the necessary functions from the calculator_1 module """
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    """ Printing the addition,subtraction, multiplication, Devision"""
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
