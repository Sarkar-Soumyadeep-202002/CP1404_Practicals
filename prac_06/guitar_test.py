from prac_06.guitar import Guitar


def main():
    """Start the program"""
    first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    second_guitar = Guitar("Another guitar", 2013, 10000.00)
    print("Gibson get_age() - Expected 100, Got {}".format(first_guitar.get_age()))
    print("Another get_age() - Expected 9, Got {}".format(second_guitar.get_age()))
    print("Gibson is_vintage() - Expected True, Got {}".format(first_guitar.is_vintage()))
    print("Another is_vintage() - Expected False, Got {}".format(second_guitar.is_vintage()))


main()
