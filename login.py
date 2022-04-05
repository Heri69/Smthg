import time

jmeno = "heri"
heslo = "rakel"

jmeno_input = input("Jmeno: ")
heslo_input = input("heslo: ")

if jmeno_input == jmeno and heslo_input == heslo:
    print("Pristup povolen")
    print("pockej")
    time.sleep(3)
    print("Loadim")
    time.sleep(1)
    print("...")
    print("Bla bla bla mas to povelny")
elif jmeno_input == jmeno and heslo_input != heslo:
    print("mas blbe heslo")
elif jmeno_input != jmeno and heslo_input == heslo:
    print("mas ble jmeno")
else:
    print("napsal si to picusky")
#