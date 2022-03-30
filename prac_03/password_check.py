"""
Name: Soumyadeep Sarkar
Description: Checks for the validity of a password and prints '*' according to the length of the password
"""


def is_valid(password, length):
    return len(password) <= length  # Checks if the length of the password is within the given length


def main():
    password = input("Enter the password: ")
    length = 10
    print(f"Your password is Valid? {is_valid(password,length)}")
    for character in range(0, len(password)):
        print('*', end='')  # Prints the same number of asterisks as the length of the password


main()
