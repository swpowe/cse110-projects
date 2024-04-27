# W04 Prepare: Learning Activities
# https://byui.instructure.com/courses/295034/quizzes/4603115?module_item_id=35255260

# While Loops #1
# number = -1

# while number < 0:
#     number = int(input('Please type a positive number: '))
#     if(number < 0):
#         print('Sorry, that is a negative number. Please try again.')
    
# print(f'The number is: {number}')

# While Loops #2
# answer = ''

# while answer.lower() != 'yes':
#     answer = input('May I have a piece of candy? ')
    
# print('Thank you!')






# For Loops
# colors = ["red", "blue", "green", "yellow"]

# for i in colors:
#     print(i)

# for i in range(1, 9):
#     print(i)

# for i in range(2, 21, 2):
#     print(i)
    


# Looping Through Strings
word = "Commitment"
favorite_letter = input("What's your favorite letter? ")

for letter in word:
    if letter.lower() == favorite_letter.lower():
        # print(letter.upper(), end="")
        print("_", end="")
    else:
        print(letter.lower(), end="")
        
