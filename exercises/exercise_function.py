#!/usr/bin/env python3
"""
Exercise: Writing Your Own Function

Instructions:
1. Define a function named 'multiply' that takes two arguments and returns their product.
2. In the main function, ask the user to input two numbers.
3. Use your 'multiply' function to calculate the product of the two numbers.
4. Print the result.
5. Hint: Convert input strings to numeric types as needed.
"""

def multiply(a, b):
    # TODO: Return the product of a and b.
    return a * b

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Use the multiply function to compute the product.
    result = multiply(num1, num2)
    print("The product of the numbers is:", result)

if __name__ == '__main__':
    main()
