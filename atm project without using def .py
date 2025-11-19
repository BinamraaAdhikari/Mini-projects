users={"Raj":"raj1234",
       "Shyam":"hello123",
       "Sita":"sita32456",
       "Rama":"nepal123"}

balance={"Raj":1000,
         "Shyam":5000,
         "Sita":65,
         "Rama":50000}

for i in range(3):
    username=input("Enter your username:")
    if username not in users:
        print("No users found")
        continue
    
    
    else:
        for x in range(3):
            b=input("Enter your password:")
            if b!=users[username]:
                print("Wrong Password")
                continue 
            else:
                print("Welcome back",username)
                break
        break
else:
    print("Too many attempts try again later.")
    exit()



while True:
    print("Enter a number for the option you want to choose:")
    print("1) Check Balance.\n2) Deposit money\n3) Withdraw Money.\n4)Exit")
    choice=int(input("Enter a number for the option you want to select:"))
    if choice<1:
        print("Invalid number. Try again")
        continue
    elif choice>4:
        print("Invalid number.Try again")
        continue
    elif choice==1:
        print("Your current balance is:",balance[username])
        continue
    elif choice==2:
        deposit=int(input("Enter the amount of money you want to deposit:"))
        if deposit<1:
            print("Invalid amount")
            continue
        else:
            newdeposit=balance[username]+deposit
            balance[username]=newdeposit
            print("Your updated amount is",balance[username])
        continue
    elif choice==3:
        withdraw=int(input("Enter the amount of money you want to withdraw:"))
        if withdraw<1:
            print("Invalid amount")
            continue
        else:
            newwithdraw=balance[username]-withdraw
            if withdraw>balance[username]:
                print("Insufficient amount")
                continue
            else:
                balance[username]=newwithdraw
                print("Your remaining balance is",balance[username])
                continue
    elif choice==4:
        print("Logging out.\nThanks for using the ATM.",username,"Please come again")
        exit()
    else:
        print("Invalid character")
        continue
