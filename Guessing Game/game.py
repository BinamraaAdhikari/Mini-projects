import random
while True:
    c=random.randint(1,100)
    for i in range(7):
        a=int(input("Please select a random number between 1 to 100:"))
        if a==c:
            print("You win")
            break
        elif a<0:
            print("Only numbers above 0. Please try again")
        elif a>100:
            print("Only numbers below 100. Please try again")
        elif a>c:
            print("You are higher than the required number")
        elif a<c:
            print("You are lower than the required number")
        
    else:
        print("Game Over. The correct number was",c)
    while True:
        print("Do you want to play again?")
        y=input("yes or no?:").lower()
        if y=="yes":
            print("Lets play the game again")
        elif y=="no":
            print("Thanks for playing")
            exit()
        else:
            print("Please answer in either yes or no:")            
