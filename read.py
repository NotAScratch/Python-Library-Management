def read():
    file = open("laptop", "r")
    laptop_id = 1
    mydict = {}

    for line in file:
        line = line.replace("\n", "")
        lines = line.split(",")
        mydict.update({laptop_id: lines})
        laptop_id += 1
    file.close()
    return mydict


def laptops():
    mydict = read()
    print("S.N \t Name \t\t Brand \tPrice \tQuantity \tChipset \t\tGraphics")
    for sn, laps in mydict.items():
        print(f"{sn}\t{laps[0]:10}\t\t{laps[1]:10}\t{laps[2]:10}\t{laps[3]:10}\t\t{laps[4]:10}\t{laps[5]:10}")
