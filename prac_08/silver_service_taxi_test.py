"""
CP1404 Practical
Author: Soumyadeep Sarkar
Description: Program to test the SilverServiceTaxi class
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Start the program"""
    taxi1 = SilverServiceTaxi("Hummer", 200, 4.0)
    print(f"The fare for the current trip is ${taxi1.calculate_fare(75.59)}")
    print(taxi1)


main()
