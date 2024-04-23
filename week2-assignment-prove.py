# 02 Prove: Assignment - Word Games

# The other day, I was really in trouble. It all started when I saw a very
# [adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
# I could think to do was to [verb] over and over. Miraculously,
# that caused it to stop, but not before it tried to [verb]
# right in front of my family.

# Capitalize Exclamation

def print_story():
    print("Your story is: ")
    print(f"""The other day, I was \x1B[3mreally\x1B[0m in trouble.
It all started when I saw a very {adj} {animal} {verb1} down the hallway. 
"{exclamation.upper()}!" I yelled. But all I could think to do was to {verb2} over and over.
Miraculously, that caused it to stop,
but not before it tried to {verb3} right in front of my family.""")
    print()

print("Please enter the following:")
print() #blank line
adj = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
print() #blank line

print_story()
