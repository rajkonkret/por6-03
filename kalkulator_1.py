print("""
    Kalkulator
    """)

a = int(input("Podaj liczbe"))
b = int(input("Podaj liczbe druga"))
odp = input("1. Dodawanie, 2. Odejmowanie, 3. Mnożenie, 4. Dzielenie")

if odp == "1":
    print(f"Wynik dodawania {a} + {b} =", a + b)
elif odp == "2":
    print(f"Wynik odejmowania {a} - {b} =", a - b)  # nie potrzeba spacji p
elif odp == "3":
    print(f"Wynik mnozenia {a} * {b} =", a * b)
elif odp == "4":
    if b != 0:
        print(f"Wynik dzielenie {a} / {b} =", a / b)
    else:
        print("Nie dziel przez zero")
else:
    print("nie znam takiego działania")