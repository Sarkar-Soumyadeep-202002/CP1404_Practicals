"""
CP1404 Practical
Author: Soumyadeep Sarkar
Description: Program to test the UnreliableCar class
"""
from unreliable_car import UnreliableCar


def main():
    """Start of the program"""
    test = UnreliableCar("Comfort-Delgro", 100, 85)
    test.drive(50)
    print(test)


main()
