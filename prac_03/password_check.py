"""
Name: Soumyadeep Sarkar
Description: Checks for the validity of a password and prints '*' according to the length of the password
"""


def get_password():
    password = input("Enter your password: ")
    return password


def print_asterisk(password):
    for character in range(0, len(password)):
        print('*', end='')


def main():
    password = get_password()
    length = 10
    print(f"Your password is Valid? {len(password) >= length}")
    print_asterisk(password)


main()
