#!/usr/bin/python3

# Importing the necessary module
import sys

# Checking the number of command-line arguments
if len(sys.argv) != 4:
    print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
    sys.exit(1)

# Importing the necessary functions from the calculator_1 module
from calculator_1 import add, sub, mul, div

# Parsing the command-line arguments
a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])
result = 0

# Performing the desired operation based on the provided operator
if operator == "+":
    result = add(a, b)
elif operator == "-":
    result = sub(a, b)
elif operator == "*":
    result = mul(a, b)
elif operator == "/":
    result = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

# Printing the result of the operation
print("{} {} {} = {}".format(a, operator, b, result))
