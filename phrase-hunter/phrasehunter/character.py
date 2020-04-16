# Create your Character class logic in here.

class Character:
    # Note: when creating member functions in Python, the
    # first argument for a standard member function should always be
    # `self`, which will be set to the instance of that class
    def __init__(self, char):
        # Set an instance variable we call `original`
        # to the parameter `char`
        # Use an assertion (`assert`) to make sure
        # the input char is of length 1
        assert len(char) == 1
        self.original = char
        self.was_guessed = False

    def __repr__(self):
        """
        By modifying the __repr__ member function,
        we modify how this class is represented
        as a string.
        This makes it easy to customize the result of
        e.g. print or str calls on this object.
        """
        if self.was_guessed:
            return self.original
        return "_"
