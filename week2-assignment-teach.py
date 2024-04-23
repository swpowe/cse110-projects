# 02 Teach - ID Badge

# First name, Last name, Email Address, Phone Number, Job Title, ID Number

# The last name should be converted from whatever the user types to be displayed in ALL CAPS.

# The job title should be displayed so that the first letter is capitalized.

# The email address should be displayed in all lowercase.
def print_ID_card():
    print()
    print("The ID Card is:")
    print("--------------------------------------")
    print(f"{lastName.upper()}, {firstName.title()}")
    print(f"{title.title()}")
    print(f"ID: {id}")
    print()
    print(f"{email.lower()}")
    print(f"{phone}")
    print()
    print(f"{'Hair:' + hair:<20} Eyes: {eyes}")
    print(f"{'Month:' + month:<20} Training: {training}")
    print("--------------------------------------")


print("Please enter the following information:")
print()
firstName = input("First name: ")
lastName = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
title = input("Job title: ")
id = input("ID number: ")
hair = input("Hair: ")
eyes = input("Eyes: ")
month = input("Month: ")
training = input("Training: ")

print_ID_card()