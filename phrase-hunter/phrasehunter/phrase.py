"""
Python Development Techdegree
Project 3 - Phrase Hunters
Author: Felix Andrew Sapalaran (felixandrewsapalaran@gmail.com)
---------------------------------------------------------------
"""

# Create your Phrase class logic here.
from .character import Character


class Phrase:
    def __init__(self, phrase):
        # Store input parameter phrase as an instance attribute
        # called phrase

        # Here we use a "list comprehension" to store
        # a collection of Characters generated from the
        # input letters
        # Loosely speaking, a list comprehension is like a
        # shorthand for-loop where the statement on the
        # left inside the square brackets is used to initialise
        # each item in the list from elements pull out from the
        # iterable on the right
        self.phrase = [Character(char) for char in phrase]

    def has_been_guessed(self, guess):
        """
        Checks if a character, `char`, has already been
        guessed or not
        """
        for char in self.phrase:
            if char.original == guess and char.was_guessed:
                return True
        return False

    def guess_letter(self, guess):
        """
        Checks a letter against all characters, and if
        it matches, sets those character.was_guessed values
        to true
        """
        result = False
        for char in self.phrase:
            if char.original.lower() == guess:
                char.was_guessed = True
                result = True
        return result

    def display(self):
        """
        Simple display function that converts each
        character to a string (using just str(char) as we
        set the __repr__ function of Character) and
        returns the character representations separated by
        spaces.
        """
        print(" ".join(str(char) for char in self.phrase))

    def all_guessed(self):
        """
        Convenience method to check if all
        letters have been guessed
        """
        return all(char.was_guessed for char in self.phrase)
