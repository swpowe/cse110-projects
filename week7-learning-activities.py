# # Learning Activity 1 of 2
# def display_regular(message):
#     print(message)
    
# def display_uppercase(message):
#     print(message.upper())
    
# def display_lower(message):
#     print(message.lower())
    
# message = input("What is your message?")

# display_regular(message)
# display_uppercase(message)
# display_lower(message)

# -------

# # Learning Activity 2 of 2
# import math

# def compute_area_square(side1):
#     return compute_area_rectangle(side1, side1)

# def compute_area_rectangle(side1, side2):
#     return side1 * side2

# def compute_area_circle(radius):
#     return math.pi * (radius ** 2)

# running = True

# while(running):
#     print("What kind of shape do you have?")
#     selection = int(input("1. Square\n2. Rectangle\n3. Circle\n4. Quit\n>"))
#     area = 0
    
#     if selection == 1:
#         side = int(input("What is the length of a side? "))
#         area = compute_area_square(side)
#     elif selection == 2:
#         side1 = int(input("What is the length of your first side? "))
#         side2 = int(input("What is the length of your second side? "))
#         area = compute_area_rectangle(side1, side2)
#     elif selection == 3:
#         radius = float(input("What is the radius? "))
#         area = round(compute_area_circle(radius), 2)
#     elif selection == 4:
#         running = False
#     else: 
#         print("Please enter a valid number between 1-4")
    
    
#     if selection != 4:
#         print(f"Area is: {area}")

def display_numbers(x, y):

    print(x)
    
display_numbers(3,3)
