#!/usr/bin/env python3
"""
Exercise: Using Conditionals

Instructions:
1. Ask the user to input a number.
2. Write code to check if the number is even or odd.
3. Print "The number is even" if it's even, and "The number is odd" if it's odd.
4. Hint: Use the modulo operator (%) to determine evenness.
"""

def main():
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("That's not a valid integer. Please try again.")
        return

    # TODO: Check if the number is even or odd.
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

if __name__ == '__main__':
    main()
