from abc import ABC, abstractmethod


class Ptak(ABC):
    """"
    Klasa opisujaca Ptaka
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lece z szybkoscia", self.szybkosc)

    @abstractmethod
    def wydaj_odgłos(self):
        pass


class Orzel(Ptak):
    """
    To ja orzeł
    """

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")

    def wydaj_odgłos(self):
        print("piiiii")


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odgłos(self):
        print("ko ko ko")


#
# orzel = Ptak("orzel", 5)
# print(orzel.gatunek)
# orzel.latam()


orzel = Orzel("orzel", 5)
orzel.poluj()
orzel.latam()

# kura = Ptak("Kura", 0)
# kura.latam()
# kura.wydaj_odgłos()

kura_2 = Kura("kura")
kura_2.latam()
kura_2.wydaj_odgłos()
