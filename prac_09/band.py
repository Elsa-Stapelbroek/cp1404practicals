"""CP1404 practical 9 - Intermediate exercise 3: Association, not inheritance"""


class Band:
    """Represent a Band object."""
    def __init__(self, name, ):
        """Initialise a Band instance."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band instance."""
        return f"{self.name} ({', '.join([str(member) for member in self.members])})"

    def add(self, musician):
        """Add a Musician to Band members list."""
        self.members.append(musician)

    def play(self):
        """Return a string introducing each member and their first (or no) instrument."""
        return '\n'.join([member.play() for member in self.members])
