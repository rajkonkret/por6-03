odejmij = lambda a, b: a - b

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosly")

print(odejmij(5, 6))
print(wiek(5))
print(wiek(11))
print(wiek(21))

lista = [1, 2, 7, 10, 55]
print(f"Zastosowanie map:{list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie filter:{list(filter(lambda x: x < 3, lista))}")
print(f"Zastosowanie filter:{list(filter(lambda x: x > 8, lista))}")
print(f"Zastosowanie filter:{list(filter(lambda x: 3 < x < 20, lista))}")
#14:30