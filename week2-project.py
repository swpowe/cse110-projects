# Meal Prep
# I added logic asking the user if they'd like to pay a tip and if so how much
# Ask the user for the following:
# The price of a child's meal (floating point)
# The price of an adult's meal (floating point)
# The number of children (integer)
# The number of adults (integer)

# Determine the meal's subtotal (before adding sales tax) by multiplying the 
# number of children by the price of their meal, and multiplying the number of adults by the price 
# of their meal and adding those two values together.

# Display the subtotal.
# Ask the user for the sales tax rate as a percentage (floating point). 
# Please note that this percentage should be entered and stored as a number such as 6, or 6.5, not 0.06 or 0.065.

# Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.
# Compute and display the total price of the meal by adding the subtotal and the sales tax.

# Ask the user for the the payment amount (floating point)

# Compute and display the change.
price_child = float(input("What's the price of a child's meal? "))
price_adult = float(input("What's the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
print()
subtotal = (price_child * children) + (price_adult * adults)
print(f"Subtotal: ${subtotal:.2f}")
print()
sales_tax_rate = float(input("What's the sales tax rate? "))
sales_tax = (subtotal * sales_tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")
# ask if they'd like to add a tip
# if yes then ask for percent
# if no continue
add_tip = input("Would you like to add a tip (y/n)?")
if(add_tip == 'y'):
    percent_tip = float(input("What percent tip? "))
    tip = (total * percent_tip) / 100
    total = total + tip
    print(f"Your new total is ${total:.2f}")
payment = float(input("What is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}")