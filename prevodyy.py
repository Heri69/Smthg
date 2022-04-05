def menu():	
	print("\n")
	print("1 - Prevod kilometry na mile")
	print("3 - Prevod mile na kilometry")	
	print("3 - Vypnuti programu\n")

def kilometrynamile():
	print("1 - Kilometry na mile?")
	print("2 - Mile na kilometry?\n")
	prevodmilnakm = int(input("Vyber[1-2]: "))
	if prevodmilnakm == 1:
    		cislo1 = float(input("Zadej cislo v kilometrech: "))
    		print("V milích to je: ", cislo1 * 0.6214, "mil\n")   		
	elif prevodmilnakm == 2:
    		cislo2 = float(input("Zadej cislo v mili: "))
    		print("V kilometrech to je: ", cislo2 / 0.6214, "km\n")
    		

def Farentheitynacelsia():
	print("1 - Celsia na farentheity")
	print("2 - Farentheity na celsia\n")
	prevodstupnu = int(input("Vyber[1-2]: "))
	if prevodstupnu == 1:
    		cislo3 = float(input("Zadej cislo v clesiich: "))
    		prevodnik1 = cislo3 * 1.8
    		print("Ve farentheitech to je: ", prevodnik1 + 23 , "farentheitu\n" )
	elif prevodstupnu == 2:
    		cislo4 = float(input("Zadej cislo v farentheitech: "))
    		prevodd = cislo4 - 32   
    		print("Ve celsiech to je: ", prevodd / 1.8, "celsia\n")

def konec():
	print("Program se vypnul :(")
	print()	
	exit(0)


menu()
odpoved = int(input("Vyber [1-3]: "))
while odpoved != 3:	
	if odpoved == 1:    		
    		kilometrynamile()
	elif odpoved ==2:   		
    		Farentheitynacelsia()
	menu()
	odpoved = int(input("Vyber [1-3]: "))
konec()
