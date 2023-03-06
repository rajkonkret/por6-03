dictionary = {}
print(dictionary)
dictionary["imie"] = "radek"
print(dictionary)
print(dictionary['imie'])
dictionary["wiek"] = "39"
print(dictionary)

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

lista = [44, 55, 66, 88]
dictionary["liczby"] = lista
print(dictionary)
print(dictionary["liczby"])
print(dictionary["liczby"][0])
lista_2 = [1, 2, 3, 4]
nowa_lista = lista_2 + lista
print(nowa_lista)

dictionary_2 = {'imie': ['Radek', 'Tomek']}
print(dictionary_2)

dictionary_3 = {'imie': 'name\'s', 'kot': 'cat'}
print(dictionary_3['imie'])

# print("Mamy w słowniku ", dictionary_3.keys())
# key = input("Podaj wyraz do przetłumaczenia")  # odczytanie z klawiatury
# print(dictionary_3[key])
# 14:40
dictionary_3.update({"pies": "dog"})
print(dictionary_3)

a = 6
b = 7
a = float(input("Podaj liczbe"))  # rzutowanie na int
b = float(input("Podaj liczbe"))
print(a + b)
