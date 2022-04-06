"""
Name: Soumyadeep Sarkar
Description: Program to accept a number from the user and print that many number of lines each having 6 random numbers
             between 1 and 45 sorted in ascending order."""
import random


def main():
    """Accept a number from the user and display that many lines with each line having 6 random numbers between 1
    and 45 sorted in ascending order."""
    quick_picks = int(input("How many quick picks? "))
    for item in range(0, quick_picks):
        count = 0
        numbers = []
        while count < 6:
            num = random.randint(1, 45)
            if num in numbers:
                continue
            numbers.append(num)
            count += 1

        numbers.sort()
        number_constant = tuple(numbers)
        for i in number_constant:
            print(i, end=' ')

        print()


main()
