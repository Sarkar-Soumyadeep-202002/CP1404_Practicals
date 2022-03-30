import random
print(random.randint(5, 20))  # line 1 Ans: On line1, we can see a random number being selected between 5 and 20. The smallest number we could have seen is 5 and the largest one is 20.
print(random.randrange(3, 10, 2))  # line 2 Ans: On line2, we see a random odd number between 3 and 10 being selected. 3 is the smallest possible number. Line 2 cannot produce 4 as it only displays odd numbers.
print(random.uniform(2.5, 5.5))  # line 3 Ans: On line 3, we get a random floating point number between 2.5 and 5.5. 2.5 was the smallest possible number. Largest is 5.5.
# Code
print(random.randint(1,100))