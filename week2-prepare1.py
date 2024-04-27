# Learning activity 1 numeric
# Prompt the user for their age.
# Convert it to a number, add one to it, and tell them how old they will be on their next birthday.

# Prompt the user for the number of egg cartons they have.
# Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.

# Prompt the user for a number of cookies and a number of people.
# Then, divide the number of cookies by the number of people to determine how many cookies each person gets.

age = input("Please enter your age: ")
print(f"Next year you will be {int(age) + 1}")

eggs = input("How many egg cartons do you have? ")
print(f"You have a total of {int(eggs) * 12} eggs.")

cookies = input("How many cookies do you have? ")
people = input("How many people are there? ")
print(f"Each person gets {int(cookies) // int(people)} cookie(s).")