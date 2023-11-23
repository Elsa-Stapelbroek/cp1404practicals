"""
CP1404 practical 9 - Intermediate exercise 1: Unreliable Car, class

estimate: 35 minutes
actual: 30 minutes
"""
from random import uniform
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of Car that includes reliability percentage."""
    def __init__(self, reliability: float, **kwargs):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car if the generated number is lower than the reliability."""
        if uniform(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
