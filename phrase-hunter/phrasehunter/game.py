# Create your Game class logic in here.
# We'll need the random module (built-in to the standard library in Python)
# in order to select a random phrase
import random
# Use the string library as a convenience to quickly reference
# all lowercase characters
from string import ascii_lowercase
from .phrase import Phrase


class Game:
    """
    Main game class that controls the game state
    and runs the main loop
    """
    def __init__(self, phrases):
        """
        This is the initialisation member function (loosely speaking the
        same as a constructor in e.g. C++), which is called when
        the class is instantiated
        """
        # Set an instance attribute called phrases (self.phrases)
        # equal to the input parameter phrases
        self.phrases = [
            phrase.lower().strip() for phrase in phrases]
        # We also start off with no active phrase
        # and an empty list of guessed letters
        self.active_phrase = None
        self.guessed_letters = []

    def run(self):
        """
        This is the game's main loop, which
        keeps playing a new game until the user decides not to
        play any more
        """
        while True:
            self.play_game()
            if input("Do you want to play again? [yN]").strip().lower() != "y":
                break
        print("Thank you for playing phrasehunter, good-bye!")

    def play_game(self):
        """
        This is the core game loop, which
        repeatedly displays the current phrase (masking
        un-guessed letters) and prompts for input
        """
        # We initialize the state of the game here
        # Select the current run's active phrase
        self.active_phrase = Phrase(random.choice(self.phrases))
        # Reset the guessed letters to an empty list
        self.guessed_letters = []
        # Set the remaining_guesses to the full number
        remaining_guesses = 5
        has_won = False
        # Start playing!

        # The loop continues while we have remaining
        # guesses
        while remaining_guesses > 0:
            # game's display phrase allows us to
            # call the phrase.display function but also
            # add any additional output (like a new line)
            # which wouldn't necessarily make sense to be
            # included in the phrases display member function.
            self.display_phrase()

            # Next we prompt the user to input a letter
            # this member function handles bad inputs
            # and will only return once a valid letter
            # has been selected
            letter = self.prompt_for_guess()

            # We now pass the letter into a make_guess
            # member function, which checks if our guess
            # was good or not, and adds the letter to the
            # list of guessed letters
            good_guess = self.make_guess(letter)
            # If False is returned, we didn't guess correctly
            if not good_guess:
                remaining_guesses -= 1
                print(
                    "Oops! You have", remaining_guesses,
                    "/5 remaining!")
            else:
                # if it was a good guess, we need to check for
                # a win - for now this is just a light
                # wrapper around phrases all_guessed function
                has_won = self.check_win()
            if has_won:
                print("Congratulations, you won!")
                return
        print("You lose, better luck next time!")

    def display_phrase(self):
        """
        Displays the active phrase, hiding any guessed
        letters
        """
        self.active_phrase.display()
        print("")

    def prompt_for_guess(self):
        """
        Prompts the user for a guess repeatedly
        until a valid letter is chosen. If an invalid
        letter is chosen, a message lets the user know why
        (handled in is_valid_guess)
        """
        while True:
            letter = input("Guess a letter: ")
            print("")
            # Allow blanks by stripping them with strip
            # and ignore case by converting all to lower-case
            # using lower
            letter = letter.lower().strip()
            if self.is_valid_guess(letter):
                break
        return letter

    def is_valid_guess(self, letter):
        """
        Checks if lettter is a valid guess
        and if not displays a useful message to the user
        """
        if len(letter) != 1 or letter not in ascii_lowercase:
            print("Invalid character entered")
            return False
        if self.active_phrase.has_been_guessed(letter):
            print("You already guessed that, please enter a different letter")
            return False
        if letter in self.guessed_letters:
            print("You already guessed that, please enter a different letter")
            return False
        return True

    def make_guess(self, letter):
        """
        Calls the active phrase's guess_letter function
        and also adds the letter to the list of guessed_letters
        """
        # By here we should have a valid letter
        # So we can pass it into the active phrases
        # checking function
        result = self.active_phrase.guess_letter(letter)
        self.guessed_letters.append(letter)
        return result

    def check_win(self):
        """
        Checks if the user has won - just calls
        the current active_phrase's all_guessed function
        """
        return self.active_phrase.all_guessed()
