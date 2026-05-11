# user input
try:
    x = int(input("Zadej cislo: "))
except ValueError:
    print("Chyba: nezadal jsi cislo!")

# division
try:
    a = int(input("Zadej prvni cislo: "))
    b = int(input("Zadej druhe cislo: "))
    print("Vysledek:", a / b)
except ValueError:
    print("Chyba: musis zadat cisla!")
except ZeroDivisionError:
    print("Chyba: nelze delit nulou!")

# file reading
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Chyba: soubor neexistuje!")
