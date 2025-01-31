#!/usr/bin/env python3
"""
Advanced Challenge: Simple Calculator

For students who want an extra challenge, this project creates a simple calculator.
You will:
- Implement basic arithmetic operations.
- Handle user input and perform calculations based on a menu choice.
- Consider edge cases like division by zero.

Try to extend the functionality as an extra exercise (e.g., looping until exit).
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Handle division by zero
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("Welcome to the Advanced Calculator Challenge!")
    print("Enter two numbers and choose an operation.")
    
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", subtract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
    else:
        print("Invalid choice. Please try again.")
    
    # Extra Challenge:
    # Modify the calculator to allow multiple calculations (loop until the user chooses to exit).

if __name__ == '__main__':
    main()
