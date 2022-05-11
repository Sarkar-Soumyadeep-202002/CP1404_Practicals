"""
CP1404 Practical
Author: Soumyadeep Sarkar
Description: Program to create a Taxi Simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_input_menu(menu, bill_status, bill):
    """Display the menu, the Bill status, the bill and accept the user's choice."""
    print(bill_status, bill)
    print(menu)
    choice = input(">>> ")
    return choice


def main():
    """Start the Taxi Simulator"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    menu = "q)uit, c)hoose taxi, d)rive"
    print("Let's drive!")
    print(menu)
    choice = input(">>> ")
    choice = choice.lower()
    previous_choice = choice
    bill = 0.0
    bill_status = "Bill to Date: $"
    taxi_number = -1
    while choice != 'q':
        if choice == 'd':
            if previous_choice != 'c' or taxi_number == -1:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    taxis[taxi_number].start_fare()
                    taxis[taxi_number].drive(distance)
                    cost_of_trip = taxis[taxi_number].get_fare()
                    bill += cost_of_trip
                    print(f"Your {taxis[taxi_number].name} trip cost you ${cost_of_trip}")
                except ValueError:
                    print("Invalid distance")
            previous_choice = choice
            choice = display_input_menu(menu, bill_status, bill)
            choice = choice.lower()
        elif choice == 'c':
            print("Taxis available:")
            previous_choice = choice
            for taxi in taxis:
                print(taxi)
            try:
                taxi_number = int(input("Choose taxi: "))
                if taxi_number >= len(taxis) or taxi_number < 0:
                    taxi_number = -1
                    print("Invalid taxi choice")
            except ValueError:
                taxi_number = -1
                print("Invalid taxi choice")
            choice = display_input_menu(menu, bill_status, bill)
            choice = choice.lower()
        else:
            print("Invalid option")
            previous_choice = choice
            choice = display_input_menu(menu, bill_status, bill)
            choice = choice.lower()
    print("Total trip cost: $", bill)
    print("Taxis are now:")
    for taxi in taxis:
        print(taxi)


main()
