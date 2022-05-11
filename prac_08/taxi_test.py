"""
CP1404 Practicals
Name: Soumyadeep Sarkar
Description: Program to test the Taxi class
"""
from taxi import Taxi


def main():
    """Create object of Taxi class and use its methods."""
    taxi1 = Taxi("Prius 1", 100, 1.23)  # Create object of Taxi class
    taxi1.drive(40)
    print(taxi1)
    taxi1.start_fare()
    taxi1.drive(100)
    print(taxi1)


main()
