"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Start the program"""
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_records = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_records.append(parts)

    input_file.close()
    return subject_records


main()
