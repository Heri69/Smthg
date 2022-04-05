import random as rn
import os
penis = rn.randint(1, 10)

def menu():
    print("1 - Hra random cisla")
    print("2 - Konec \n")

def rakel ():
    print("\n")
    print("More program tohle je ")
    hadak = int(input("hadej cislo 1-10 rakovino: "))
    if hadak == penis:
        print("Uhodls to teplousi cg cg \n")
    elif hadak < penis:
        print("neni to spravne cislo kokote \n")
    elif hadak > penis:
        print("je to moc velky cislo\n")
    elif hadak != penis:
        print("male cislo geji \n")
    else:
        print("spatny vse vse vse \n")

def end():
    print("program is gonan end more ")
    os.system("pause")
    exit(0)

while True:
    menu()
    vyber = int(input("moznost v menu vyber: "))
    if vyber == 1:
        rakel()
    elif vyber == 2:
        end()
    else: 
        print("vsechno pojebane")  