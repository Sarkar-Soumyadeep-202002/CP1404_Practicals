class ProgrammingLanguage:
    """Represents comparisons of different programming languages"""

    def __init__(self, name, typing, reflection, year):
        """Initialise the different information about the programming languages"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the language is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        return "{}, {}, Reflection = {}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                      self.year)
