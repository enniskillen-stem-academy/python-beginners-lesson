#!/usr/bin/env python3
"""
Working with Loops

In this lesson, you will:
- Learn about for loops and while loops.
- See examples of iterating over a range of numbers.
- Understand how loops help you repeat tasks.

Read the comments and try the extra challenge provided.
"""

def main():
    # For loop example: Print numbers 1 through 5.
    print("For loop example:")
    for i in range(1, 6):
        print(i)

    # While loop example: Count down from 5 to 1.
    print("\nWhile loop example:")
    count = 5
    while count > 0:
        print(count)
        count -= 1

    # Challenge:
    # Write a loop that calculates and prints the sum of numbers from 1 to 100.
    # (Hint: Use a loop and a variable to accumulate the sum.)

if __name__ == '__main__':
    main()
