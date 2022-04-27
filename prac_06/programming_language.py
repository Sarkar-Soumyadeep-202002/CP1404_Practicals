class ProgrammingLanguage:
    """Represents comparisons of different programming languages"""

    def __init__(self, typing, reflection, year):
        """Initialise the different information about the programming languages"""
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the language is dynamic"""
        return self.typing == "Dynamic"

    