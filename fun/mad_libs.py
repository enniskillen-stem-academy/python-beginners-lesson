#!/usr/bin/env python3
"""
Mad Libs Game

In this fun activity, you'll provide a few words (nouns, adjectives, verbs, etc.) and the program will
create a silly story using your inputs. Follow the prompts and enjoy the humorous result!

For advanced students: Try to add more input prompts or create additional stories.
"""

def main():
    print("Welcome to the Mad Libs Game!")
    
    # Ask for user input
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    # Create the story using the input words
    story = (
        f"Today, I went to the {place} and saw a {adjective} {noun} "
        f"that could {verb} like no other!"
    )
    
    # Display the story
    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == '__main__':
    main()
