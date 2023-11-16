"""CP1404 practical 9 - Intermediate exercise 2: SilverServiceTaxi, class"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that calculates fare based on fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, fanciness: float, **kwargs):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall value."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate fare like parent Taxi, but add flagfall as well."""
        return super().get_fare() + self.flagfall
