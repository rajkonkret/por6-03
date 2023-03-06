lista = [44, 55, 66, 77, 33, 22, 11, 55, 33, 11]
zbior = set(lista)
print(zbior)

zbior.add(18)

# print(zbior)
# print(zbior.pop())
# print(zbior.pop())
# print(zbior.pop())
# print(zbior)
# zbior.remove(55)
# print(zbior)
zbior_2 = {66, 11, 44, 18, 55, 62, 999}
print(zbior_2)
print(zbior | zbior_2)
print(zbior & zbior_2)
print(zbior - zbior_2)
print(zbior.difference(zbior_2))
print(zbior_2.difference(zbior))
