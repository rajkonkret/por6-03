lista = []
print(lista)
lista.append("Radek")
lista.append("Radek")
lista.append("Radek")
lista.append("Radek")

print(lista)
lista.insert(1, "DArek")
print(lista)
lista.append(12)
print(lista)
lista[1] = "Ania"  # podstawienie wartosci pod konkretny index
print(lista)
lista.remove("Ania")
print(lista)
lista.remove("Radek")
print(lista)
lista.remove("Radek")
print(lista)
lista.reverse()
print(lista)

lista_2 = lista.copy()
lista.remove(12)
print(lista)
print(lista_2)

liczby = [54, 999, 34, 22, 12.54, 687]
print(liczby)
liczby.sort()
print(liczby)
liczby.reverse()
print(liczby)
liczby_2 = liczby.copy()
liczby.clear()
print(liczby)
print(liczby_2)
liczby_2[0] = 6666
print(liczby_2)
print(liczby_2[0:3])
print(liczby_2[:3])
print(liczby_2[2:])
print(liczby_2[:-1])
print(liczby_2)
print(len(liczby_2))  # długosc kolekcji 6, indexy 0..5
liczby_2.remove(54)
print(len(liczby_2))
print(liczby_2)
print(liczby_2.pop(2))  # usuniecie liczby na konkretnym indexie
print(liczby_2)

krotka = tuple(liczby_2)
print(krotka)