#!/usr/bin/python3

def add_arg(argv):
    """
    Add the command-line arguments and print the sum.
    Args:
        argv: List of command-line arguments.
    """
    # Count the number of arguments passed (excluding the script name itself)
    n = len(argv) - 1

    # If no arguments are provided, print 0 and return
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        i = 1
        add = 0
        # Iterate over the arguments and add them
        while i <= n:
            add += int(argv[i])
            i += 1
        # Print the sum of the arguments
        print("{:d}".format(add))

if __name__ == "__main__":
    import sys
    # Call the add_arg function with the command-line arguments
    add_arg(sys.argv)
