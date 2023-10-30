"""Guitar class."""

CURRENT_YEAR = 2023
VINTAGE_MINIMUM = 50


class Guitar:
    """Represent Guitar object."""

    def __init__(self, name="", year=0, cost=0.0):  # prac guide says default for cost should be 0?
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return Guitar information in formatted string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Determine the age of a Guitar in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine whether a Guitar is vintage based on its age and the minimum vintage age."""
        return self.get_age() >= VINTAGE_MINIMUM
