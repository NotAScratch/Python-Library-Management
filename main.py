from functions import buy_function
from functions import sellfun

continueLoop = True

while continueLoop:
    print("\n")
    print("\t\tWelcome to Bahndrey laptop shop")
    print("\t\tAddress: Rani Pokhari")
    print("_____________________________________________________________")
    print("Please select below options")
    print("_____________________________________________________________")
    print("\n")
    print("Press 1 to buy from manufacturer")
    print("Press 2 to sell to customer")
    print("Press 3 to exit from program")
    print("\n")
    print("_____________________________________________________________")
    print("_____________________________________________________________")

    try:
        userinput = int(input("Press from above mentioned options -> "))
        if userinput == 1:
            buy_function()
            break
        elif userinput == 2:
            sellfun()
            break
        elif userinput == 3:
            print("THANK YOU VISIT AGAIN")
            continueLoop = True
        else:
            print("Invalid input. Please enter a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid option.")
