# # W05 Prepare: Learning Activities
# # Part 1 - Lists
# friends = []
# friend = ""

# while friend != "End":
    
#     friend = input("Type the name of a friend: ").lower().capitalize()
    
#     if friend != "End":
#         friends.append(friend)

# if len(friends) == 0:
#     print("I'm sorry you feel you have no friends.\nYou always have at least one friend.")

# elif len(friends) == 1:
#     print("Your friends name is: ")
    
#     for friend in friends:
#         print(friend)
        
# elif len(friends) > 1:
#     print("Your friends are: ")
    
#     for friend in friends:
#         print(friend)


# Part 2 - List Indexes
items = []
item = ""

print("Please enter the items of the shopping list (type: quit to finish) :")

while item != "Quit":
    item = input("Item: ").lower().capitalize()
    
    if item != "Quit":
        items.append(item)

print("\nThe shopping list is: ")

for i in range(len(items)):
    print(items[i])
    
print("\nThe shopping list with indexes is: ")

for i in range(len(items)):
    print(f"{i}. {items[i]}")

change_index = int(input("\nWhat item would you like to change? "))
new_item = input("What is the new item? ").lower().capitalize()

items[change_index] = new_item

print("\nThe shopping list with indexes is: ")

for i in range(len(items)):
    print(f"{i}. {items[i]}")
        
