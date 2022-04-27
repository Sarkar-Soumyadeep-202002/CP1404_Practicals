from prac_06.guitar import Guitar


def main():
    """Start the program"""
    print("My guitars!")
    name = input("Name: ")
    all_guitars = []
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        all_guitars.append(guitar)
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")
    index = 1
    print("""
    Name:
            
    ...snip...
             
    These are my guitars:
          """)
    for guitar in all_guitars:
        if guitar.is_vintage():
            vintage_string = "vintage" if guitar.is_vintage() else "not vintage"
            print(f"Guitar {index + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
        print(f"Guitar {index + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}")
        index += 1


main()
