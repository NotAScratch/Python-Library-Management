from read import read
from invoice import invoice
from read import laptops
from invoice import remove_after_sold
from invoice import add_when_buying


def buy_function():
    """Function to buy laptops from manufacturers and add to own stock using lists, loops and primitive data types """

    print("Please fill in your details: ")
    shop_name = input("Shop Name -> ")
    shop_address = input("Address  -> ")
    shop_number = input("Shop Number -> ")
    orders = []
    laptop_list = []

    more = True
    while more:
        while True:
            try:
                laptop_name = input("Enter the name of laptop: ")
                laptop_brand = input("Enter the brand of laptop: ")
                laptop_price = int(input("Enter the price of laptop: "))
                laptop_quantity = int(
                    input("Enter the no  of laptops that you want to buy: "))
                laptop_cpu = input("Enter the CPU of laptop: ")
                laptop_gpu = input("Enter the GPU of laptop: ")
                break
            except ValueError:
                print(
                    "Invalid input! Please enter a valid integer for the price and quantity.")

        laptop_list.append((laptop_name, laptop_brand, laptop_price,
                           laptop_quantity, laptop_cpu, laptop_gpu))
        add_when_buying(laptop_list)

        total_price = laptop_quantity * laptop_price

        orders.append((laptop_name, laptop_quantity,
                      laptop_price, total_price))

        buy_more = input("Want more laptop (yes/no)")
        if buy_more.lower() == "yes":
            more = True
        elif buy_more.lower() == "no":
            more = False
        else:
            print("Please Enter Correct Answer")

    invoice(shop_name, shop_address, shop_number, orders)


def sellfun():
    """Function to sell laptops to customers and remove from own stock using lists, loops and primitive data types """
    print("Please fill in your details: ")
    shop_name = input("Name -> ")
    shop_address = input("Address  -> ")
    shop_number = input("Number -> ")

    mydict = read()
    folder = "bill name"
    orders = []
    more = True
    while more:
        print("\n")
        laptops()

        while True:
            try:
                laptop_id = int(
                    input("Enter the SN of the laptop you want to buy: "))
                if laptop_id not in mydict:
                    print("Wrong SN Number")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        print("\n")
        while True:
            try:
                no_of_laptops = int(
                    input("How many Laptops do you want to buy: "))
                laptop_in_stock = mydict[laptop_id][3]
                if no_of_laptops <= 0 or no_of_laptops > int(laptop_in_stock):
                    print("NOT AVAILABLE")
                    laptops()
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        laptop_name = mydict[laptop_id][0]
        laptop_price = int(mydict[laptop_id][2])
        tol_price = no_of_laptops * laptop_price
        sub = int(laptop_in_stock) - no_of_laptops
        remove_after_sold(laptop_id, sub)
        orders.append((laptop_name, no_of_laptops, laptop_price, tol_price))

        want_more = input("Want more laptop (yes/no)")
        if want_more.lower() == "yes":
            more = True
        elif want_more.lower() == "no":
            more = False
        else:
            print("Please Enter Correct Answer")

    invoice(shop_name, shop_address, shop_number, orders)
