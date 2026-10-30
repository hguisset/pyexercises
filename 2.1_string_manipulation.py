"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a sentence entered by the user
# 2. Process: apply four different text transformations to the sentence and display the results
# 3. Out: the transformed versions of the sentence
# 4. My four transformations, and when each is useful: 
#    - upper(): useful for titles or text that needs emphasis.
#    - lower(): useful for standardizing text before comparisons.
#    - strip(): useful for removing unwanted spaces in user input.
#    - replace(): useful for correcting or changing specific words.


# Your code below
sentence = input("Enter a sentence: ")

print("UPPERCASE:", sentence.upper())
print("lowercase:", sentence.lower())
print("No extra spaces:", sentence.strip())
print("Replace 'ESG' with 'Sustainability':", sentence.replace("ESG", "Sustainability"))

# - upper(): worked as expected, all letters became uppercase.
# - lower(): worked as expected, all letters became lowercase.
# - strip(): worked as expected, spaces at the beginning and end were removed.
# - replace(): worked as expected, the chosen word was replaced.