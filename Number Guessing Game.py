import random

print("Welcome to my NUmber Guessing Game. You have to guess a number and if your guess is correct you will up your score.")
print("Lets PLAY")

ran = input("Enter any number you like: ")

#Check whether the given inputs has digits or not
if ran.isdigit( ):
    ran = int(ran)
    
    if ran <= 0:
        print("Please enter a number larger than 0 next time!")
        quit()

else:
    print("Please enter a number next time!")   
    quit() 

random_num = random.randrange(0,ran+1) #Guess only one number.The value got by python randomly does not change

print()
print(f"Guess the number which is in 0 - {ran} range ")
print()

#Calculate the total attempts according to the user input
if ran<=10:
    tot_attempts = (ran/2)+2
else:
    tot_attempts = round(ran/2)

print(f"You have only {tot_attempts} attempts")

chance = 0
attepmts = 0
score = 0

while chance<=(tot_attempts):
    print()
    qs = input("Make a guess: ")
    
    if qs.isdigit( ):
        qs = int(qs)

    else:
        print("Please enter a number!")   
        continue   #bring back to the starting point of the loop
        
    if qs != random_num:
        print()
        print("Your guess is WRONG!")
        chance += 1
        attepmts +=1
        print(f"You have only {tot_attempts-attepmts}")
        continue
        
    else:
        print() 
        print("Your guess is correct")
        attepmts +=1
        score += 1
        break
if score == 0:
    print("You LOSE :(")
else:
    print("Congratulations!!!")
    print()
    print(f"You won the game by {attepmts} attempts")
#add some features like difficullity modes, some helps for the player
#error with attempts