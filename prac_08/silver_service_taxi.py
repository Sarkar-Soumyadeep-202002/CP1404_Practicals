"""
CP1404 Practicals
Name: Soumyadeep Sarkar
Description: Program to create a SilverServiceTaxi class which inherits the Taxi class and uses its methods.
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Inherit the Taxi class"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize the attributes of the objects of the SilverServiceTaxi class"""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def calculate_fare(self, distance):
        """Calculate the fare of the trip"""
        super().drive(distance)
        return super().get_fare()

    def __str__(self):
        """Return a string about the Silver service taxi and its current fare"""
        return "{} plus flagfall of ${}".format(super().__str__(), SilverServiceTaxi.flagfall)
