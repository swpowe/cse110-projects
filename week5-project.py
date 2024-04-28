# Project 05: Shopping Cart
## Added a budget and alerted the user if over budget and by how much
## Aligned list into columns for display

# For this project, the user will be given a menu and have the ability to choose items from the menu. The options in the menu include the following:

# Add a new item
# Display the contents of the shopping cart
# Remove an item (only needed for the final project deliverable)
# Compute the total (only needed for the final project deliverable)
# Quit

# When the user chooses one of these options, the program should perform 
# the appropriate action. Then the program should show them the menu again,
# and allow them to choose another option. It should continue running until the user choose the option to quit.

items = []
prices = []

running = True

print("Welcome to the Shopping Cart Program!")
budget = float(input("Please enter your budget. $"))
print()
# menu
while running:
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    choice = int(input("Please enter an action: "))
    
    if choice == 1:
        item = input("What item would you like to add? ").lower().capitalize()
        price = float(input(f"What is the price of '{item}'? $"))
        
        items.append(item)
        prices.append(price)
        print(f"'{item}' has been added to the cart.")
        
        print()
        
    elif choice == 2:
        print("The contents of the shopping cart are:")
        for i in range(len(items)):
            
            print(f"{i + 1}. {items[i]:<15} ${prices[i]:.2f}")
            
            # col1 = str(i + 1) + ". " + str(items[i])
            # col2 = "$" + str(prices[i])
            # print(f"{col1} {col2:>20}")
            
        print()
        
    elif choice == 3:
        item_index = int(input("Which item number would you like to remove? ")) - 1
        
        item = items[item_index]
        
        items.pop(item_index)
        prices.pop(item_index)
        
        print(f"Item {item} was removed.")
        
        print()
        
    elif choice == 4:
        total = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
        
        if total > budget:
            print(f"You're over your ${budget:.2f} budget by ${total - budget:.2f}.\nPerhaps you should remove something.")
            print()
        else:
            print("Great Job! You stayed within budget!")
            print()
        
    elif choice == 5:
        running = False
        print("Thank you. Goodbye.")
    else:
        print("Please choose a number between 1-5.")
    
    

    
    
