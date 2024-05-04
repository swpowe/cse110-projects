# Week 5 Team Activity 
# type a list of numbers. Type 0 to finish the list
running = True
numbers = []
sum = 0
average = 0.0
largest = 0

print("Please enter a whole number to add it to the list.\nType '0' to end the list.")

while running:
    number = int(input("Enter a number: "))
    
    if number == 0:
        running = False
    else:
        numbers.append(number)

for number in numbers:
    sum += number
    if number > largest:
        largest = number

average = sum / len(numbers)

print()
print(f"The sum is : {sum}")
print(f"The average is : {average}")
print(f"The largest number is : {largest}")


# sum, average, largest