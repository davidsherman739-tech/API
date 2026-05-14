try:
    cislo1 = int(input("Zadej první číslo: "))
    cislo2 = int(input("Zadej druhé číslo: "))

    vysledek = cislo1 / cislo2

    print(f"Výsledek je: {vysledek}")

except ValueError:
    print("Musíš zadat číslo.")

except ZeroDivisionError:
    print("Nelze dělit nulou.")
