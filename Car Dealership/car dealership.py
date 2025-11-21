class car():
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    
    def getinfo(self):
       print("The",self.name,"is available in",self.color,"with a price of",self.price)
cars = [
        car("Toyota Corolla", "White", 1500000),
        car("Honda Civic", "Black", 1800000),
        car("Suzuki Swift", "Red", 1200000),
        car("Hyundai Elantra", "Blue", 2000000),
        car("Ford Mustang", "Red", 5500000),
        car("Kia Seltos", "Grey", 2200000),
        car("Mahindra Thar", "Green", 1700000),
        car("BMW 3 Series", "Black", 4500000),
        car("Audi A4", "White", 5000000),
        car("Mercedes C-Class", "Silver", 6000000)]
    


user=input("Hello Sir and Welcome. Please state your name:")
print("\nWelcome",user,"Would you like to search a car according to your budget or would uou like to see the catalog of the cars available?")
print("\nSelect the number you want to choose.")

while True:
    choice=(int(input('''\n1)List of cars available
    2)Budget:\n''')))
    if choice<=0 or choice>2:
        print("Invalid option. Please Select again")
        continue
    elif choice==1:
        print("\nThe list of cars available for purchase are:\n",)
        for i, c in enumerate(cars, start=1):
            print(i,")",end="")
            c.getinfo()
            continue
        while True:
            choice2=input("Choose a car you would like to buy or type exit to go back:\n")
            if choice2=="exit":
                print("Exiting")
                break
               
            choice3=int(choice2)
            if choice3<=0 or choice3>10:
                print("Invalid option please select again") 
                continue
            elif choice
           
