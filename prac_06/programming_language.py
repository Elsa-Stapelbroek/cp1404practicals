"""class Programming Language"""


class ProgrammingLanguage:
    """Represent a Programming Language."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise Programming Language object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return object description in formatted string."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine whether the language uses dynamic or static typing."""
        return self.typing == "Dynamic"
