
licznik = 0
while True:
    licznik += 1
    print("Komunikat")
    if licznik == 10:
        break

print(licznik)
licznik = 0

while licznik < 10:
    print("Komunikat")
    licznik += 1

# lista = []
# while True:
#     wej = input("Podaj liczbe")
#     if wej.lower() == "s":
#         break
#     lista.append(wej)
# print(lista)

while True:
    print("""
        Kalkulator
        """)

    a = int(input("Podaj liczbe"))
    b = int(input("Podaj liczbe druga"))
    odp = input("1. Dodawanie, 2. Odejmowanie, 3. Mnożenie, 4. Dzielenie, 5. Koniec")

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
    elif odp == "5":
        break
    else:
        print("nie znam takiego działania")