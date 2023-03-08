# funkcje
a = 1
b = 10


def dodaj():
    print("Wynik", a + b)


def dodaj_2():
    return a + b


def dodaj_3(a, b):
    return a + b


def dodaj_4(a=5, b=6, c=0):
    return a + b + c


def odejmij(a, b):
    return a - b


def pomnoz(a, b):
    return a * b


def oblicz_vat(cena, vat):
    return cena * (100 + vat) / 100


oblicz_vat_2 = lambda cena, vat: cena * (100 + vat) / 100

odejmij_2 = lambda a, b: a - b

print(odejmij_2(5, 4))
print(oblicz_vat(100, 23))
print(oblicz_vat_2(100, 23))

print(dodaj())
print(dodaj_2())
print(dodaj_3(5, 9))
print(dodaj_3(5, 9))
print(dodaj_4(5, 9))
print(dodaj_4(5, 9, 6))
print(dodaj_4())

print(odejmij(7, 5))
print(pomnoz(5, 4))

print(odejmij(b=7, a=9))

x = 7
print(dodaj_3(x, 8))
print(pomnoz(dodaj_3(x, 8), odejmij(b=7, a=9)))
