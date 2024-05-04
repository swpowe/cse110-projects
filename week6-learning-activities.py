# # Learning Activity (1 of 2): Working with Files
# with open("files/books.txt") as raw_data:
#     for line in raw_data:
#         cleaned_line = line.strip()
#         print(cleaned_line)
        
# Learning Activity (2 of 2): Data in Files
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# Write a program to find the youngest person in the list.
# Consider following these steps to build up to the finished program:
# Iterate through the list and display each string to the screen.
# Split the string into a name and age and print them to the screen.
# Find the age that is the youngest.
# Keep track of the name of the person that is the youngest.
youngest_age = 50
youngest_person = ""

for person in people:
    name = person.split(" ")[0]
    age = int(person.split(" ")[1])
    
    if age < youngest_age:
        youngest_age = age
        youngest_person = name
        
        print(youngest_age)

print(f"The youngest person is: {youngest_person}.\nThey are {youngest_age} years old.")