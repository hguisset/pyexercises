"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of ESG project budgets
# 2. Process: add all budgets together and divide by the number of budgets to calculate the average
# 3. Out: the average budget as a number
# 4. My function name, and why return rather than print: my function is called calculate_average_budget because its name clearly explains what it does


# Your code below

# Function definition
def calculate_average_budget(budget_list):
    if len(budget_list) == 0:
        return 0

    total = sum(budget_list)
    average = total / len(budget_list)
    return average


# Lists of ESG project budgets
budgets1 = [1200, 950, 1500, 1100, 2000, 1750, 1300, 1600]
budgets2 = [800, 1000, 1200, 1400, 1600]
budgets3 = [2500, 2200, 1800, 2100]

# Call the function three times
result1 = calculate_average_budget(budgets1)
result2 = calculate_average_budget(budgets2)
result3 = calculate_average_budget(budgets3)

# Display the results
print("Average budget list 1:", result1)
print("Average budget list 2:", result2)
print("Average budget list 3:", result3)

# Empty list test
print("Average budget empty list:", calculate_average_budget([]))


# A function should return a value because the result can then be reused in other calculations, stored in a variable, or displayed later. If the function only prints the result, the value cannot easily be used elsewhere in the program.

# If the list is empty, the function returns 0. This behaviour is acceptable because it avoids a division-by-zero error and clearly indicates that no budget data is available.