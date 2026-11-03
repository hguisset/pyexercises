"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of ESG project budgets
# 2. Process, function by function: 
#   - get_total_budget() calculates the total budget.
#   - get_number_of_projects() counts how many budgets are in the list.
#   - calculate_average_budget() calculates the average budget.
#   - is_average_budget_above_1400() uses the other three functions to determine whether the average budget is greater than 1400.
# 3. Out: True if the average budget is above 1400, otherwise False
# 4. The question my fourth function answers:  "Is the average ESG project budget above 1400?"


#Test cases for the three small functions:

#1. get_total_budget([100, 200, 300])
#   Expected output: 600

#2. get_number_of_projects([100, 200, 300])
#   Expected output: 3

#3. calculate_average_budget([100, 200, 300])
#   Expected output: 200


# Your code below

# Function 1: calculate the total budget
def get_total_budget(budget_list):
    return sum(budget_list)


# Function 2: count the number of budgets
def get_number_of_projects(budget_list):
    return len(budget_list)


# Function 3: calculate the average budget
def calculate_average_budget(budget_list):
    if len(budget_list) == 0:
        return 0

    total = get_total_budget(budget_list)
    count = get_number_of_projects(budget_list)

    return total / count


# Function 4: answer a question using the other functions
def is_average_budget_above_1400(budget_list):
    average = calculate_average_budget(budget_list)
    return average > 1400


# ESG project budgets
budgets = [1200, 950, 1500, 1100, 2000, 1750, 1300, 1600]

# Test the three small functions
print("Total budget:", get_total_budget(budgets))
print("Number of projects:", get_number_of_projects(budgets))
print("Average budget:", calculate_average_budget(budgets))

# Use the fourth function
print("Is the average budget above 1400?", is_average_budget_above_1400(budgets))

