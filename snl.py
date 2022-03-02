import random
from time import sleep

def stepFurther(step, maxStep):
    while step < maxStep :
        step += 1
        print(str(step))
        sleep(1.0)

        if step == 10:
            break

def stepUp(step, maxStep):
    while step < maxStep:
        step += 1
        print(str(step))
        sleep(1.0)         
    playerTile[playerCount] = step
    return playerTile[playerCount]   

def stepDn(step, maxStep):
    while step > maxStep:
        step -= 1
        print(str(step))
        sleep(1.0)         
    playerTile[playerCount] = step
    return playerTile[playerCount]    

maxPlayerCount = int(input("Enter number of players : "))
# cast int(), double() etc to NOT cast to str #

while maxPlayerCount < 1 or maxPlayerCount > 4:
    maxPlayerCount = int(input("The range must be between 1 to 4! \nEnter number of players : "))

ewok = "The number of players is : {}"
print(ewok.format(maxPlayerCount))

playerCount = 0
playerTile = list((0, 0, 0, 0))


while playerCount <= maxPlayerCount :
    
    print("Player " + str(playerCount+1) + "'s turn!")
    
    something = input("Type \"roll\" to roll the dice : ")

    while something != "roll":
        something = input("That is not \"roll\"! \nType \"roll\" to roll the dice : ")

    sleep(1.0)
    dice = random.randint(1, 6)
    print("You went " + str(dice) + " steps!")
    sleep(1.0)

    step = playerTile[playerCount]
    maxStep = step + dice

    stepFurther(step, maxStep)

    playerTile[playerCount] += dice

    if (playerTile[playerCount] < 10):
        print("Your place is now : " + str(playerTile[playerCount]))
    else :
        print("Your place is now : 10")    

    if playerTile[playerCount] >= 10:
        print("Player " + str(playerCount+1) + " won!")
        break

    elif playerTile[playerCount] == 3:
        print("You got a ladder! Forward 4 steps.")
        step = playerTile[playerCount]
        maxStep = step + 4
        stepUp(step, maxStep)
        print("Your new place : " + str(playerTile[playerCount]))

    elif playerTile[playerCount] == 8:

        step = playerTile[playerCount]
        stepDown = 2
        maxStep = step-stepDown
        print("Oh no, you got a snake! You need to go back " + str(stepDown) + " spaces.")
        stepDn(step, maxStep)
        print("Your new place : " + str(playerTile[playerCount]))

    playerCount += 1

    if playerCount > maxPlayerCount-1:
        playerCount = 0