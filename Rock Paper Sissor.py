import random

values = ['rock', 'paper', 'sissor']

while True:
    user_inp = input("Rock, Paper, Sissor: ").lower() #by usnig .lower(), you can covert user input to lowercase
    system_pick = random.randrange(0,3)
    system_inp = values[system_pick]
    print(f"You picked {user_inp}")
    print(f"System picked {system_inp}")

    if user_inp == system_inp:
        print("Tie")
        continue
    elif (user_inp == "rock" and system_inp == "paper") or (user_inp == "sissor" and system_inp == "rock") or (user_inp == "paper" and system_inp == "sissor"):
        print("You Lose")
    else:
        print("You Win")
    

    #add quit option , how many time player win