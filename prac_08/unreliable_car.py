"""
CP1404 Practicals
Author: Soumyadeep Sarkar
Description: Program to inherit the Car class and use its methods.
"""
import random
from prac_06.car import Car


class UnreliableCar(Car):
    """Inherit the Car class."""

    def __init__(self, name, fuel, reliability):
        """Initialize the attributes of the objects of the UnreliableCar class"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        reliability_check = random.randint(0, 100)
        if reliability_check > self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
