user = "Radek"
wiek = 39
wersja = 3.90001
liczba = 134632344532

# print(type(liczba))
# print(print.__doc__)  # dokumentacja
#
# print("Witaj %s masz teraz %d lat" % (user, wiek))
# print("Witaj %(user)s masz teraz %(age)d lat" % {"user": user, "age": wiek})
# print("Witaj {} masz teraz {} lat".format(user, wiek))
# print(f"Witaj {user} masz teraz {wiek} lat")
# # %s - string, %d - digit - liczba

print("Uzywamy wersji Python %i" % 3)
print("Uzywamy wersji Python %f" % 3.9)
print("Uzywamy wersji Python %.1f" % 3.9)
print("Uzywamy wersji Python %.f" % 3.9)
print("Uzywamy wersji Python {}".format(wersja))
print(f"Uzywamy wersji Python {wersja:.1f}")
print(f"Uzywamy wersji Python {wersja:.0f}")
print(f"{user:>20}")
print(f"{user:>10}")
print(f"{user:<10}")

print(liczba)
print("Nasza duża liczba {:,}".format(liczba).replace(',', '.'))
print("Nasza duża liczba {:,}".format(liczba).replace(',', ' '))
print("Nasza duża liczba {:,}".format(liczba))
print("Nasza duża liczba {:_}".format(liczba))
print("Nasza duża liczba {:X}".format(liczba))
print("Nasza duża liczba {:x}".format(liczba))
print("Nasza duża liczba {:b}".format(liczba))
