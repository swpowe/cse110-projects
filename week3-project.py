# # Adventure Game
## I added a lot of logic including a while loop so the user can exit or play again to try other scenarios.

# You need to have at least three levels of scenarios with possible choices. 
# (This means that every time the user plays the game they should answer at least 
# three questions because every branch of the game should go three levels deep.)

# Scenarios that follow an earlier answer should be handled with nested if statements. 
# In other words, the body/block of the first if statement will contain a print 
# statement and then another if statement inside it.

# At least one of your scenarios must have more than two possible choices.

# In each prompt, write the choices in ALL CAPS, so that the user knows which 
# words are possible responses to choose.

# Responses should be words (strings) rather than numbers.

# When checking the users responses, you should match on the keyword, regardless of 
# the uppercase/lowercase used in the response (e.g., "match", "MATCH", "Match" should all work).

# Making different choices should take you to different scenarios. 
# (You shouldn't have the same result for different choices.)

# Choices should only work for the correct question.

# In other words, if one scenario resulted in choices of Run/Hide, but another 
# resulted in choices Follow/Look, you should not be able to respond with "Follow" 
# to the question that asked for Run/Hide.

# A good way to accomplish this is to have a series of nested if statements. 
# (That is, the print and then the next if statement will be within the body/block of the first if statement.)

# For each question, you should provide an "else" clause to handle the case that the 
# user tries to type something other than the possible choices. It is up to you how to handle this case.
game = True

while game:
    choice = input("You're walking along a dark, winding road\nand you see a glowing light in the distance.\nDo you want to turn to INVESTIGATE the light \nor CONTINUE on your journey? ")

    if choice.lower() == "investigate":
        
        choice = input("You turn to walk toward the light and walk\nabout 100 steps when suddenly you fall into a pit.\n\nDo you try to CLIMB out or sit and WAIT for help? ")
        
        if choice.lower() == "climb":
            
            choice = input("You claw your way up the side of the pit and\nwhen you reach the top you stumble on the group to catch your breath.\n\nAfter you've rested, do you CONTINUE toward the light or give up and TURN around? ")
            
            if choice.lower() == "continue":
                
                choice = input("You continue on your way and eventually arrive \nat an old farmhouse where a farmer and his dog are sitting on the porch.\n\nThey invite you in and you enjoy a delicious meal.\n\n Would you like to play AGAIN or EXIT ")
                
                if choice.lower() == "again":
                    game = True
                else:
                    game = False
            
            elif choice.lower() == "turn":
                
                choice = input("You decide to turn around and eventually get back to the road and continue on your way.\n\nPlay AGAIN or EXIT ")
                
                if choice.lower() == "again":
                    game = True
                else:
                    choice = input("I'm sorry, I don't understand that choice. Exiting.")
        
                    game = False
            else:
                choice = input("I'm sorry, I don't understand that choice. Exiting.")
        
                game = False
        elif choice.lower() == "wait":
            choice = input("You sit in the pit for about 30 mins waiting for someone to come and rescue you.\nUnfortunately,\nno one comes but you and you die...\n\nPlay AGAIN or EXIT? ")
            if choice.lower() == "again":
                game = True
            elif choice.lower() == "exit":
                game = False
            else:
                choice = input("I'm sorry, I don't understand that choice. Exiting.")
        
                game = False
                

    elif choice.lower() == "continue":
        # continue logic
        choice = input("You shrug your shoulders and continue on your way.\n\nBefore too long, you hear the sound of footsteps behind you. \n\nDo you TURN and look or do you RUN? ")
        
        if choice.lower() == "turn":
            choice = input("As you turn around, you discover the noise came\nfrom your friend BOB that had been following you.\n\nPlay AGAIN or EXIT? ")
            
            if choice.lower() == "again":
                game = True
            elif choice.lower() == "exit":
                game = False
            else:
                choice = input("I'm sorry, I don't understand that choice. Exiting.")
                game = False 
            
        elif choice.lower() == "run":
            choice = input("You run as hard as you can until you're\ncompletely out of breath.\nAt this point you feel safe so you stop to rest.\nAfter sitting for a few minutes, you hear a rustling in the bushes.\nYou cower in fear hoping to survive the night when something jumps from the bushes! \n\nWas it a WEREWOLF or a LEPRECHAUN? ")
            
            if choice.lower() == "warewolf":
                choice = input("That's too bad. You died.\n\nPlay AGAIN or EXIT? ")
                
                if choice.lower() == "again":
                    game = True
                elif choice.lower() == "exit":
                    game = False
                else:
                    choice = input("I'm sorry, I don't understand that choice. Exiting.")
                    game = False 
                
            elif choice.lower() == "leprechaun":
                choice = input("YAY! You got a pot of gold!\n\nPlay AGAIN or EXIT? ")
                
                if choice.lower() == "again":
                    game = True
                elif choice.lower() == "exit":
                    game = False
                else:
                    choice = input("I'm sorry, I don't understand that choice. Exiting.")
                    game = False 
                                    
            else:
                choice = input("I'm sorry, I don't understand that choice. Exiting.")
        
                game = False
        else:
            choice = input("I'm sorry, I don't understand that choice. Exiting.")
        
            game = False
    
    else:
        choice = input("I'm sorry, I don't understand that choice. Exiting. ")
        
        game = False




