#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    # Get a list of all names defined in the hidden_4 module
    names = dir(hidden_4)

    # Iterate over each name and print it if it is not a special name starting with "__"
    for name in names:
        if name[:2] != "__":
            print(name)
