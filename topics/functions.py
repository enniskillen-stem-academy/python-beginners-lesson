#!/usr/bin/env python3
"""
Introduction to Functions

In this lesson, you will:
- Learn how to define and call functions.
- See examples of reusable code with functions.
- Get a challenge to write your own function.

Read the code comments and complete the challenge when you’re ready.
"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Return the sum of a and b."""
    return a + b

def main():
    # Example: Using functions.
    print(greet("Student"))

    # Example: Adding two numbers.
    result = add_numbers(5, 7)
    print("5 + 7 =", result)

    # Challenge:
    # Write your own function that multiplies two numbers.
    # Then, call your function with sample values and print the result.
    #
    # For example:
    # def multiply(a, b):
    #     return a * b
    #
    # product = multiply(3, 4)
    # print("3 * 4 =", product)

if __name__ == '__main__':
    main()
