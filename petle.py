import random

lista = []

for i in range(0, 10, 2):  # od 0..9 co 2
    print(i)

for i in range(10):
    if i % 2 == 0:
        print(i)

for i in range(6):
    print(random.randrange(1, 50))

lista_2 = list(range(1, 50))
print(lista_2)

for i in range(6):
    wyn = random.choice(lista_2)
    print(wyn)
    lista_2.remove(wyn)
