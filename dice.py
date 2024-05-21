import random

score = 0

while (score < 21):

    prompt = 'e'

    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
        
    score = roll1 + roll2 + score

    print("Roll 1: " + str(roll1))
    print("Roll 2: " + str(roll2))
    print("Current score: " + str(score))
        
    if (score < 21):
        
        while (prompt.upper() != "YES") and (prompt.upper() != "NO"):
            
            prompt = input("Would you like to roll again? ") 

            if (prompt.upper() != "YES") and (prompt.upper() != "NO"):
                print("Invalid choice. (Only 'yes' and 'no')")
                
        if (prompt.upper() == "NO"):
            break
        
if (score == 21):
    print("You WON!")

elif (score > 21):
    print("You LOST!")
    
else:
    roll3 = random.randint(15,21)
    print("Final Roll: " + str(roll3))

    if (roll3 > score):
        print(str(roll3) + ">" + str(score))
        print("You LOST!")
        
    else:
        print("You WON!")