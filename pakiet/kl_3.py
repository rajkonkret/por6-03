# PEP8
class Dom:
    """
    To jest klasa Dom
    """

    def __init__(self, metraz, kolor, ilosc_okien):
        self.__metraz = metraz
        self.kolor = kolor
        self.__ilosc_okien = ilosc_okien

    def sprawdz_metraz(self):
        print(self.__metraz)

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraz"))
        self.__metraz = wybor
        print("Metraz wynosi", self.__metraz)

    def zmien_kolor(self):
        wybor = input("Podaj nowy kolor")
        self.kolor = wybor
        print("Metraz wynosi", self.kolor)
        self.__farba()

    def zmien_okna(self):
        wybor = int(input("Podaj ilosc okien"))
        self.__ilosc_okien = wybor
        print("ilosc okien", self.__ilosc_okien)

    def __farba(self):
        print("Skonczyla sie farba")


dom_1 = Dom(23, "czerwony", 5)
print(dom_1.kolor)
print(dom_1)
dom_1.sprawdz_metraz()
dom_1.zmien_metraz()
dom_1.zmien_okna()
dom_1.zmien_kolor()
# 12:00
