# Programmer: Kyle Kwan
# Date 11/29/2022
# File Name: FinalProject.py
# Description: This program checks if a range of numbers is divisible by either 3 or 5.
#              The user inputs the start and end of the range.

# User inputs for both the start and the end of the range they decide.
starting_num = int(input("Please enter starting value: "))
ending_num = int(input("Please enter ending value: "))

# A "for" loop that prints the range of numbers, while printing it checks the numbers' divisibility of both 3 and 5.
for i in range(starting_num, ending_num + 1):
    # Checks if number is divisible by BOTH 3 and 5.
    if ((i % 3 == 0) & (i % 5 == 0)):
        print(i, "-- Both")
    # Checks if number is divisible by ONLY 3.
    elif (i % 3 == 0):
        print(i, "-- 3")
    # Checks if number is divisible by ONLY 5.
    elif (i % 5 == 0):
        print(i, "-- 5")
    # If the number isn't divisible by either 3 or 5 it just prints the number.
    else:
        print(i)
        
input(f"\nPress enter to exit")