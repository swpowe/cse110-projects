# # 1 of 2 If Statements
# my_fav = "lion"
# first_number = int(input("What is the first number? "))
# second_number = int(input("What is the second number? "))

# if first_number > second_number:
#     print("The first number is greater.")
# elif second_number > first_number:
#     print("The second number is greater.")
# else:
#     print("The numbers are the same!")

# fav_animal = input("What is your favorite animal? ")

# if fav_animal.lower() == my_fav:
#     print(f"The {fav_animal.lower()} is \x1B[3mmy\x1B[0m favorite too!")
# else:
#     print(f"The {fav_animal.lower()} is not my favorite. I like the {my_fav}.")
    
# 2 of 2 Complete Conditions
decision = False

print("Please answer the following questions with a number between 1-10")
loan_size = int(input("How large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

if loan_size >= 5:
    if credit >= 7 and income >= 7:
        decision = True
    elif (credit >= 7 or income >= 7) and down_payment >= 5:
        decision = True
    else:
        decision = False
elif loan_size <= 4:
    if credit < 4:
        decision = False
    elif income >= 7 or down_payment >= 7:
        decision = True
    elif income >= 4 and down_payment >= 4:
        decision = True
else:
    decision = False

if decision:
    print("Congratulations! You've been approved!")
else:
    print("I'm sorry. We can not approve you for a loan.")
