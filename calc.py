def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def krat(num1, num2):
    return num1 * num2

def deleno(num1, num2):
    return num1 / num2

print("Vyber si pocitani\n")
print("1. Plus")
print("2. Minus")
print("3. Krat")
print("4. Deleno")
print("\n")

while  True:

    choice = input("Vloz volbu( 1, 2, 3, 4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = int(input("zadej prvni cislo: "))
        num2 = int(input("zadej druhy cislo: "))

        if choice == '1':
            print(num1, "+", num2, "=", plus(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", minus(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", krat(num1, num2))

        elif choice == '4':        
            print(num1, "/", num2, "=", deleno(num1, num2))

        anotherpocet = input("Chces pocitat znova?????? (jes/ne): ")
        if anotherpocet == "ne":
            print("papa programeee")
            break


    else:
        print("si kar proste a mas to blbe\n")