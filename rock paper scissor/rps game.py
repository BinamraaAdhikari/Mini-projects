import random
game={"rock":1,
      "paper":2,
      "scissor":3}
while True:
    print("Lets play a game of Rock,Paper and Scissors\n")
    user=(input("Please input either Scissors,Rock or Paper: \n")).lower()
    if user not in game:
        print("Please input either Rock,Paper or Scissors\n ")
        continue
    else:
        cpu=random.choice(list(game.keys()))
        print("I choose:",cpu)   
    usecho=game[user]
    cpucho=game[cpu]
    if usecho==cpucho: 
        print("You chose",user,"and I chose",cpu,"so its a tie")
    elif (usecho==1 and cpucho==2) or (usecho==2 and cpucho==3) or (usecho==3 and cpucho==2):
        print("You chose",user,"and I chose",cpu,"so I win.")
    else:
        print("You chose",user,"and I chose",cpu,"so you win.")
   
         
    ask=input("Would you like to try again?(Yes/No):").lower()
    while True:
        if ask=="yes":
            print("Challenge Accepted")
            break
        elif ask=="no":
            print("Exiting the game. Thnks for playing")
            exit()
        elif ask!="yes"or"no":
            print("Please answer in either yes or no.")
            continue
