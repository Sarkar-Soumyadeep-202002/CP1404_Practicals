"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if (denominator==0): # Change made to avoid ZeroDivisionError
            print("Denominator cannot be Zero")
            return
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    print("Finished.")
main()
# 1. When will a ValueError occur?
# Ans: ValueError will occur when the user inputs a non-integer like alphabets.
# 2. When will a ZeroDivisionError occur?
# Ans: Zero division error occurs when the user inputs 0 for the denominator.
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Ans: Yes, of course.
