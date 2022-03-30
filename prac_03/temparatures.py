"""
Name: Soumyadeep Sarkar
Description: Convert temperature from celsius to fahrenheit and vice versa

"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)


def celsius_to_fahrenheit(celcius):
    """Convert Celsius to Fahrenheit"""
    return celcius * 9.0/5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return 5/9 * (fahrenheit - 32)


def main():
    """Start the Program"""
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print("Result: {:.2f} F".format(celsius_to_fahrenheit(celsius)))
        elif choice == "F":
            fahrenheit = float(input('Fahrenheit: '))
            print("Result: {:.2f} C".format(fahrenheit_to_celsius(fahrenheit)))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


main()

