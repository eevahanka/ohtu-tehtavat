KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.lukujono        

    def lisaa(self, lisattava):
        if not self.kuuluu(lisattava):
            self.lukujono[self.alkioiden_lkm] = lisattava 
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            if self.alkioiden_lkm - len(self.lukujono) == 0:
                uusi_jono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(self.lukujono, uusi_jono)
                self.lukujono = uusi_jono
            return True
        return False

    def poista(self, luku):
        if luku in self.lukujono:
            self.lukujono.remove(luku)
            self.lukujono.append(0)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True
        return False

    def kopioi_taulukko(self, vanha, uusi):
        for i in range(0, len(vanha)):
            uusi[i] = vanha[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        uusi_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            uusi_joukko.lisaa(luku)
        for luku in b_taulu:
            uusi_joukko.lisaa(luku)
        return uusi_joukko

    @staticmethod
    def leikkaus(a, b):
        uusi_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            if luku in b_taulu:
                uusi_joukko.lisaa(luku)
        return uusi_joukko

    @staticmethod
    def erotus(a, b):
        uusi_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            if luku not in b_taulu:
                uusi_joukko.lisaa(luku)
        return uusi_joukko

    def __str__(self):
        str_luvut = []
        for luku in self.lukujono:
            if luku != 0:
                str_luvut.append(str(luku))
        tuotos = "{" + ', '.join(str_luvut) + "}"
        return tuotos
