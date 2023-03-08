class Human:
    """
    To jest klasa Human opisująca człowieka w Pythonie
    """

    plec = "k"
    imie = ""
    wiek = None

    def powitanie(self):
        """
        metoda witajaca
        :return:
        """
        print("Nazywam sie", self.imie)

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w droge")
        else:
            print("Ruszyłem w droge")


czl_1 = Human()  # To jest obiekt
print(czl_1)
print(czl_1.imie)
print(czl_1.__doc__)
czl_1.imie = "Raedke"  # Nadanie wartosci polom obiektu
print(czl_1.imie)
czl_1.powitanie()
print(czl_1.plec)
print(czl_1.wiek)
czl_1.ruszaj()  # wykonanie metody na obiekcie
czl_2 = Human()
czl_2.imie = "Zenek"
czl_2.plec = "m"
czl_2.ruszaj()

czl_3 = Human()
czl_3.imie = "Anna"
czl_3.plec = "k"
czl_3.powitanie()
czl_3.ruszaj()
