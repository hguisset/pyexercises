"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: user's favorite ESG pillar and years of ESG experience
# 2. Process: ask for both pieces of information and create a sentence using them
# 3. Out: a sentence describing the user's ESG interests and experience
# 4. My two fields, and what I would do with them: I chose a favorite ESG pillar and years of ESG experience because they could be useful in sustainable finance to better understand a candidate's interests and background.



# Your code below
pillar = input("What is your favorite ESG pillar? ")
experience = int(input("How many years of ESG experience do you have? "))

print(f"You are most interested in the {pillar} pillar and have {experience} years of ESG experience.")

# - Empty line: Python raises "ValueError: invalid literal for int() with base 10: ''."
# - Space: Python raises "ValueError: invalid literal for int() with base 10: ' '"
# - Text instead of a number for years of experience: Python raises "ValueError: invalid literal for int() with base 10: 'two' because expects a number."
