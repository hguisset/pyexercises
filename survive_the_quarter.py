# ==================================================
# Python Final Exam
# Name: Hapsatou Guisset
# Group: A
# ==================================================

# QUESTION 1
# The file scenarios_A.csv contains all game scenarios.
# Each scenario has three possible decisions (A, B and C)
# with different impacts on budget and reputation.

# QUESTION 2
# One game day works as follows:
# 1. Display the day number.
# 2. Display budget and reputation.
# 3. Display the scenario.
# 4. Display options A, B and C.
# 5. Ask the player for a choice.
# 6. Update budget and reputation.
# 7. Check if the game can continue.

# QUESTION 3
# At the end of the game, the player sees:
# - Final budget
# - Final reputation
# - Final score
# - Final title
# - Best move
# - Worst move
# The result is also saved in results.csv.

# QUESTION 4
# Possible problems:
# - Invalid choice entered by the user
# - Budget becomes 0 or negative
# - Reputation becomes 0 or negative
# - Missing CSV file

# FEATURE CHOSEN
# Best Move / Worst Move
# The program stores all player decisions
# and displays the best and worst move
# at the end of the game.


# Import required modules
import csv
import random
from datetime import datetime


# Load all scenarios from the CSV file
def load_scenarios():

    scenarios = []

    with open("scenarios_A.csv", "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            scenario = {}

            scenario["text"] = row["Scenario"]

            # Option A stored as a tuple:
            # (text, budget change, reputation change)
            scenario["A"] = (
                row["OptionA"],
                int(row["BudgetA"]),
                int(row["ReputationA"])
            )

            scenario["B"] = (
                row["OptionB"],
                int(row["BudgetB"]),
                int(row["ReputationB"])
            )

            scenario["C"] = (
                row["OptionC"],
                int(row["BudgetC"]),
                int(row["ReputationC"])
            )

            scenarios.append(scenario)

    return scenarios


# Ask the player for a valid choice
def get_choice():

    choice = input("Choose A, B or C: ").upper()

    while choice not in ["A", "B", "C"]:

        choice = input("Please enter A, B or C: ").upper()

    return choice


# Update budget and reputation
# This function returns a tuple
def apply_choice(budget, reputation, option):

    budget = budget + option[1]
    reputation = reputation + option[2]

    if reputation > 100:
        reputation = 100

    return budget, reputation


# Assign a title according to final score
def get_title(score):

    if score < 95:
        return "Eternal Intern"

    elif score < 120:
        return "Growth Hacker"

    elif score < 140:
        return "CMO Material"

    else:
        return "Viral Legend"


# Save results in results.csv
def save_results(name, budget, reputation, title):

    with open(
        "results.csv",
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            name,
            budget,
            reputation,
            title,
            datetime.now().strftime("%Y-%m-%d")
        ])


# ==========================
# START OF THE GAME
# ==========================

name = input("Enter your name: ")

budget = 10000
reputation = 50

# Store player's decisions
history = []

# Load scenarios
scenarios = load_scenarios()

# Randomize scenario order
random.shuffle(scenarios)

# Main game loop
for day in range(min(10, len(scenarios))):

    scenario = scenarios[day]

    print()
    print("DAY", day + 1)

    print("Budget:", budget)
    print("Reputation:", reputation)

    print()
    print(scenario["text"])

    print()
    print("A:", scenario["A"][0])
    print("B:", scenario["B"][0])
    print("C:", scenario["C"][0])

    choice = get_choice()

    option = scenario[choice]

    budget, reputation = apply_choice(
        budget,
        reputation,
        option
    )

    print()
    print("Budget change:", option[1])
    print("Reputation change:", option[2])

    # Save player move
    history.append(
        (
            option[2],
            option[0]
        )
    )

    # Check game over conditions
    if budget <= 0:

        print()
        print("GAME OVER - Budget reached 0")
        break

    if reputation <= 0:

        print()
        print("GAME OVER - Reputation reached 0")
        break


# ==========================
# FINAL RESULTS
# ==========================

score = reputation + budget // 200

title = get_title(score)

print()
print("FINAL RESULTS")

print("Budget:", budget)
print("Reputation:", reputation)
print("Score:", score)
print("Title:", title)

# Find best and worst move
best_move = max(history)
worst_move = min(history)

print()
print("Best move:", best_move[1])

print("Worst move:", worst_move[1])

# Save results to CSV
save_results(
    name,
    budget,
    reputation,
    title
)

print()
print("Results saved in results.csv")