"""
Name: Soumyadeep Sarkar
Description: Display the result according to the score.
"""
import random


def get_result(score):
    """Find the appropriate result for the score"""
    result = ""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score < 50:
        result = "Bad"
    elif 50 <= score < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


def main():
    """Start the program"""
    score = int(input("Enter your score: "))
    print(f"{score} is {get_result(score)}")
    rand_score = random.randint(0, 100)  # Taking a random score
    print(f"{rand_score} is {get_result(rand_score)}")


main()

