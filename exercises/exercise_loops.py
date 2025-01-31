#!/usr/bin/env python3
"""
Exercise: Using Loops

Instructions:
1. Write a loop that prints the square of numbers from 1 to 10.
2. After printing, try modifying the code to print the cubes instead.
3. Bonus Challenge: Calculate and print the sum of squares from 1 to 10.
"""

def main():
    print("Squares of numbers from 1 to 10:")
    # TODO: Loop from 1 to 10 and print the square of each number.
    for i in range(1, 11):
        print(f"{i} squared is {i**2}")

    # Bonus Challenge: Calculate and print the sum of squares from 1 to 10.
    sum_of_squares = sum(i**2 for i in range(1, 11))
    print("\nSum of squares from 1 to 10 is:", sum_of_squares)

if __name__ == '__main__':
    main()
