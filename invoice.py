from datetime import date
from read import read


def invoice(name, address, phone, orders):
    ship_cost = 0
    today = date.today()
    invoice_name = f"{name}_{today}.txt"

    print("-----TRANSACTION SUCCESSFUL-------")
    with open(invoice_name, "w") as file:
        file.write("_____________________________________________________________\n")
        file.write("\t\tBhandrey Laptop Shop\n")
        file.write("_____________________________________________________________\n")
        file.write("\t\t\tINVOICE SLIP\n")
        grand_total = 0

        file.write("_____________________________________________________________\n")
        file.write("_____________________________________________________________\n")
        file.write(f" |   Name\t\t\t\t\t | {name}\n")
        file.write(f" |   Address\t\t\t\t\t | {address}\n")
        file.write(f" |   Phone\t\t\t\t\t\t  | {phone}\n")
        file.write("_____________________________________________________________\n")
        file.write("_____________________________________________________________\n")
        file.write("name \t\t price \t\t  quantity\n")
        for each in orders:
            name_lap = each[0]
            quantity = each[1]
            price = each[2]
            total_price = each[3]
            grand_total += float(total_price + (0.13 * total_price))
            file.write(f" {name_lap}\t\t{price}\t\t{quantity}\n")

        file.write("______________________________________________________________\n")
        file.write(f"_____________ |   Total Price->\t\t\t{total_price}\n")
        file.write(f"_____________ |   VAT Amount->\t\t\t{0.13 * total_price}\n")
        file.write("______________________________________________________________\n")
        file.write(f"_____________ |  Grand Total Price->\t\t {grand_total} \n")

        print("\n")
        print("\n")
        print("_____________________________________________________________\n")
        print("\t\tKamal Pokhari Laptop Shop\n")
        print("_____________________________________________________________\n")
        print("\t\t\tINVOICE SLIP\n")
        print("_____________________________________________________________\n")
        print("_____________________________________________________________\n")
        print(f" |   Name \t\t\t\t\t | {name}\n")
        print(f" |   Address  \t\t\t\t\t | {address}\n")
        print(f" |   Phone  \t\t\t\t\t  | {phone}\n")
        print("_____________________________________________________________\n")
        print("_____________________________________________________________\n")
        print("name \t\t price \t\t  quantity\n")

        for each in orders:
            name_lap = each[0]
            quantity = each[1]
            price = each[2]
            total_price = each[3]
            #grand_total = total_price + (0.13 * total_price)
            print(f" {name_lap}\t\t{price}\t\t{quantity}\n")

        print("______________________________________________________________\n")
        print(f"_____________ |   Total Price->\t\t\t{total_price}\n")
        print(f"_____________ |   VAT Amount->\t\t\t{0.13*total_price}\n")
        print("______________________________________________________________\n")
        print(f"_____________ |  Grand Total Price->\t\t {grand_total}\n")


def remove_after_sold(laptop_list, sub):
    mydict = read()
    with open("laptop", "w") as file:
        mydict[laptop_list][3] = sub
        for key, value in mydict.items():
            if key == laptop_list:
                value[3] = sub
            file.write(",".join(str(each)for each in value))
            file.write("\n")


def add_when_buying(laptop_list):
    mydict = read()
    new_key = len(mydict)+1
    for each in laptop_list:
        key = str(new_key)
        mydict[key] = list(each)
        with open("laptop", "w") as file:
            for key, value in mydict.items():
                file.write(",".join(str(each)for each in value))
                file.write("\n")
















