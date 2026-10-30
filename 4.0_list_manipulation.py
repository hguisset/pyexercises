"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of monthly ESG project budgets
# 2. Process: display the original list, display one item, display the sorted list, and calculate the total budget.
# 3. Out: the full list, one selected item, the sorted list, and the total budget.
# 4. What my list is about, and what I computed from it: My list contains monthly ESG project budgets. I computed the total budget because it shows how much money is allocated overall to ESG projects, which is useful for financial planning and reporting.


# Your code below
budgets = [1200, 950, 1500, 1100, 2000, 1750, 1300, 1600]

print("Full list:", budgets)

print("One item:", budgets[3])

print("Sorted list:", sorted(budgets))

print("Total budget:", sum(budgets))