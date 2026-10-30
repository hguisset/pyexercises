"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a number N entered by the user
# 2. Process: the program checks whether N is valid. If it is, it goes through all numbers from 1 to N and determines whether each number is odd or even
# 3. Out: a list of numbers from 1 to N with "odd" or "even" written next to each one
# 4. What happens on 0, on a negative number, on a very large number:
#    - 0: the program displays a message saying N must be greater than 0.
#    - Negative number: the program displays an error message.
#    - 5000: the program refuses the value because printing 5000 lines would not be practical.


# Your code below
n = int(input("Enter a number: "))

if n == 0:
    print("Please enter a number greater than 0.")
elif n < 0:
    print("Negative numbers are not allowed.")
elif n >= 5000:
    print("Number too large. Please enter a smaller number.")
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

# - with N = 6, there are three odd numbers (1, 3, 5) and three even numbers (2, 4, 6)
# - 0 displays a warning message "Please enter a number greater than 0."
# - a negative number displays a warning message "Negative numbers are not allowed."
# - 5000 displays a warning message "Number too large. Please enter a smaller number."
