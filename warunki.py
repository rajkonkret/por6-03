# czy_znasz_Pythona = True
# odp = input("Czy znasz pythona(t/n)")
#
# if odp == "t":
#     print("Brawo")
# else:
#     print("Musisz sie uczyc")
#     print("dwa")
#
# print("Koniec")

# podatek = 0.0
# zarobki = int(input("Podaj dochód"))
#
# if zarobki < 10000:
#     podatek = 0.05
# elif zarobki < 30000:
#     podatek = 0.1
# elif zarobki < 100000:
#     podatek = 0.15
# else:
#     podatek = 0.5
#
# print(f"Zapłącisz {zarobki * podatek} zł")
# suma_zam = 67
# if suma_zam > 100:
#     rabacik = 25
# else:
#     rabacik = 0
#
# print("suma zam", suma_zam, "rabat", rabacik)  # shift f6 - zmiana nazwwy zmiennej
#
# rabacik = 25 if suma_zam > 100 else 0
# print("suma zam", suma_zam, "rabat", rabacik)  # shift f6 - zmiana nazwwy zmiennej

lista_bledow = []
alert_system = 'email'
error = 'medium'
error_message = 'Stało sie coś strasznego'
#  :=
if alert_system == 'console':
    print(error_message)
elif alert_system == "email":
    if error == "critical":
        lista_bledow.append("critical")
    elif error == "medium":
        lista_bledow.append("medium")
    else:
        lista_bledow.append("Nieznany")

print(lista_bledow)
