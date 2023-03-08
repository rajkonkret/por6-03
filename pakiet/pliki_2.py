fh = open('dane.txt', 'a')
fh.write("Test\n")
fh.write("Test\n")
fh.write("Test\n")
fh.close()

with open('dane.txt') as fh:
    for lines in fh:
        print(lines.strip())

lista = [1, 2, 3, 4]
tmp = str(lista)
print(tmp)

lista_3 = []
with open('dane.txt') as fh:
    for lines in fh:
        print(lines.strip())
        lista_3.append(lines.strip())

print(lista_3)
print(lista_3[0])
