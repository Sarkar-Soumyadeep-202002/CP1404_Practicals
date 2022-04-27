"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    name = input("Name: ")
    my_car = Car(180, name)
    my_car.drive(30)
    print(my_car)
    limo = Car(100, name)
    limo.add_fuel(20)
    limo.drive(115)
    print(limo)


main()
