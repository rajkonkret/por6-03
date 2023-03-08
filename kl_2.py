class Human:
    """
    klasa Human
    """

    def __init__(self, imie, wiek=0, plec="k"):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        """
        metoda powitanie
        :return:
        """
        print("Nazywam sie", self.imie)

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w droge")
        else:
            print("Ruszyłem w droge")


czl_1 = Human("Radek")
print(czl_1.imie)
czl_2 = Human("Radek", 36, plec='m')
print(czl_2.wiek)
