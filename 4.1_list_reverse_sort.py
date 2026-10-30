"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of monthly ESG project budgets
# 2. Process: display the list in four different orders while keeping the original list unchanged
# 3. Out: the list shown in four different orders and the original list displayed again at the end
# 4. My four orders, and which ones modify the original: 
#    - original order: does not modify the original list.
#    - sorted ascending with sorted(): creates a copy.
#    - sorted descending with sorted(reverse=True): creates a copy.
#    - reversed with reversed(): creates a copy.
# none of these methods modify the original list because they all create a new list instead of changing it in place


# Your code below
budgets = [1200, 950, 1500, 1100, 2000, 1750, 1300, 1600]

print("Original order:", budgets)

print("Ascending order:", sorted(budgets))

print("Descending order:", sorted(budgets, reverse=True))

print("Reversed order:", list(reversed(budgets)))

print("Original list at the end:", budgets)