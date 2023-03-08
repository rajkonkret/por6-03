tuple_1 = "Tomek", "Michał", "Asia", "Kasia"
tuple_2 = "Radek",
tuple_3 = 43, 55, 22.43, 11, 200

print(tuple_1)
print(type(tuple_1))
print(tuple_2)
print(type(tuple_2))

print(tuple_3)
print(tuple_1.count("Tomek"))
print(tuple_1.index("Asia"))

name = tuple_1[2]
print(name)
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
# 13:30
tuple_1 = "Tomek", "Michał", "Asia", "Kasia"

*imie1, imie2, imie3 = tuple_1  # mamy 4 wartosc ale tdo trzech pudełek chcemy wrzucic
# Tomek, ...................,Kasia
# ...,Asia, kasia
print(imie1)
print(imie2)
print(type(imie2))
print(imie3)
print(type(imie3))

lista = list(tuple_1)
print(lista)
