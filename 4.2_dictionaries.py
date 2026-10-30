"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a dictionary describing a company using ESG-related information
# 2. Process: read a field, modify a field, remove a field, then display all remaining fields and values
# 3. Out: the updated dictionary and all its fields
# 4. My object, my five fields, and why those: my object is a company
#    - name: identifies the company.
#    - sector: shows the industry.
#    - esg_score: measures ESG performance.
#    - employees: indicates company size.
#    - country: shows where the company operates.
#    These fields are useful in sustainable finance when analyzing companies


# Your code below
company = {
    "name": "GreenFuture",
    "sector": "Renewable Energy",
    "esg_score": 82,
    "employees": 1200,
    "country": "France"
}

# Read a field
print("Company name:", company["name"])

# Change a field
company["esg_score"] = 88

# Remove a field
del company["country"]

# Access a field that may not exist
print("CEO:", company.get("CEO", "Field not found"))

# Display all fields and values
for key, value in company.items():
    print(f"{key}: {value}")

# When I tried to access a field that did not exist, Python raised a key error. Using .get() instead returns a default value and prevents the program from crashing.