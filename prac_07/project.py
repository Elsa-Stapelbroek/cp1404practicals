"""Project class"""


class Project:
    """"""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion=0):
        """Initialise a Project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        """"""
        return self.name

    def __lt__(self, other):
        """"""
        return self.priority < other.priority

    def is_completed(self):
        """Determine whether a Project is completed."""
        return self.completion == 100
