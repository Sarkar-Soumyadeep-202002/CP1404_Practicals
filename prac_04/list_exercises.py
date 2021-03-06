"""
Name: Soumyadeep Sarkar
Description: Program to accept 5 numbers and display interesting things about them.
"""


def display(numbers):
    """Display some information about the numbers"""
    average = sum(numbers) / 5
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {average}")


def main():
    """Start the program"""
    numbers = []
    for num in range(0, 5):
        number = int(input("Number: "))
        numbers.append(number)

    display(numbers)


main()


def username():
    """Check if a user can be granted access or not"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    name = input("Enter your username: ")
    if name in usernames:
        print("Access granted")
    else:
        print("Access Denied")


username()
