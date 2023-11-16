"""
CP1404 practical 9 - Intermediate exercise 1: Unreliable Car, class

estimate: 35 minutes
actual: 30 minutes
- make subclass
- add attr reliability: float between 0 and 100 (currently don't have anything ensuring the number is in that range)

- fix class docstring!
"""
from prac_09.car import Car
from random import randint  # maybe it should be a float instead?


class UnreliableCar(Car):
    """Specialised version of Car that includes reliability ..."""
    def __init__(self, reliability: float, **kwargs):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car if the generated number is lower than the reliability."""
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
