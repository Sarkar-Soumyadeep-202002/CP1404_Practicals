"""
Name: Soumyadeep Sarkar
Description: Program to display hexadecimal colour codes of different colours.
"""
HEX_COLOUR_VALUES = {"AliceBlue": "#f0f8ff", "Aqua": "#00ffff", "Black": "#000000", "Blue": "#0000ff",
                     "Brown": "#a52a2a", "Coral": "#ff7f50", "Deeppink": "#ff1493", "Gold": "#ffd700",
                     "Gray": "#bebebe", "Green": "#00ff00"}


def colour_codes():
    """Display hexadecimal colour codes for different colours entered by user."""
    colour_name = input("Colour: ")
    while colour_name != '':
        if colour_name not in HEX_COLOUR_VALUES:
            print("Invalid colour")
        else:
            print(HEX_COLOUR_VALUES[colour_name])
        colour_name = input("Colour: ")


def main():
    """Start the program."""
    colour_codes()


main()
