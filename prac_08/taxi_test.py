"""
CP1404 Practicals
Name: Soumyadeep Sarkar
Description: Program to test the Taxi class
"""
from taxi import Taxi


def main():
    taxi1 = Taxi("Prius 1", 100, 1.23)
    taxi1.drive(40)
    print(taxi1)


main()
