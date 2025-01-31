#!/usr/bin/env python3
"""
Introduction to Conditionals

In this lesson, you will:
- Learn how to use if, elif, and else statements.
- See how Python makes decisions based on conditions.

Follow the comments and try modifying the code for extra practice.
"""

def main():
    # Ask the user to enter an integer.
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer next time.")
        return

    # Check if the number is positive, negative, or zero.
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

    # Challenge:
    # Modify the code to also check if the number is even or odd.
    # Hint: Use the modulo operator (%) to determine evenness.

if __name__ == '__main__':
    main()
