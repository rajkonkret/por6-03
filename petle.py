# import random
#
# lista = []
#
# for i in range(0, 10, 2):  # od 0..9 co 2
#     print(i)
#
# for i in range(10):
#     if i % 2 == 0:
#         print(i)
#
# for i in range(6):
#     print(random.randrange(1, 50))
#
# lista_2 = list(range(1, 50))
# print(lista_2)
#
# for i in range(6):
#     wyn = random.choice(lista_2)
#     print(wyn)
#     lista_2.remove(wyn)
#
# for i in range(10):  # 0..9
#     print((i + 1) * "*")  # 5 * "*"
#
# # hackerrank
#
# for cyfra in lista_2:
#     if cyfra == 2:
#         cyfra += 1  # cyfra = cyfra + 1
#     print(cyfra)
#
# for i in range(10):
#     if i % 2 == 0:
#         print(i)
#
# list_3 = [j for j in range(10) if j % 2 == 0]
# print(list_3)
#
# names = ["Radek", "Zenek", "Marta"]
# for p in names:
#     print(p)
#
# # Radek
# # 1 Radek
#
# for i in range(len(names)):  # od0 do długosci listy czyli 3 range(3) 0..2
#     print(i + 1, names[i])
#
# for pozycja, wartosc in enumerate(names):  # pozycja  - index, wartosc = names[pozycja]
#     print(pozycja + 1, wartosc)
#
# ludzie = ["Radek", "Janek", "Asia", "Michal"]
# wiek = [47, 67, 32, 34]
# jezyk = ["java", "python"]
#
# # null None
# for p, o in enumerate(ludzie):
#     print(p, o)
#
# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])
#
# for o, w, j in zip(ludzie, wiek, jezyk):
#     print(o, w, j)

slownik = {"imie": "Grzes", "nazwisko": "Kowalski"}

for i in slownik:
    print(i)

for k, v in slownik.items():
    print(k, "=>", v)

for k in slownik.keys():
    print(k)

for k in slownik.values():
    print(k)

print({value: key for key, value in slownik.items()})
print(slownik)
