#!/usr/bin/python3

# Iterate over ASCII values for lowercase letters (a to z)
for i in range(97, 123):
    # Exclude letters 'e' (101) and 'q' (113) using an if statement
    if i not in [101, 113]:
        # Print the current character without a newline
        print(chr(i), end="")


