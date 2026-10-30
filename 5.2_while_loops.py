"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user's answer
# 2. Process:the program repeatedly asks the user to type "ESG". It counts the number of attempts and stops when the correct answer is entered or when the maximum number of attempts is reached
# 3. Out: a summary showing whether the user succeeded and how many attempts were used
# 4. My stop condition, my attempt limit, my summary:
#    - stop condition: the user types "ESG".
#    - maximum attempts: 5.
#    - "ESG", "esg", and " ESG " are accepted as the same answer by using strip() and upper().
#    - the summary contains the number of attempts and whether the user succeeded or reached the limit.


# Your code below
attempts = 0
max_attempts = 5
success = False

while attempts < max_attempts:
    answer = input("Type ESG: ").strip().upper()
    attempts += 1

    if answer == "ESG":
        success = True
        break

if success:
    print(f"Success! You entered ESG in {attempts} attempt(s).")
else:
    print(f"Maximum number of attempts reached ({max_attempts}).")