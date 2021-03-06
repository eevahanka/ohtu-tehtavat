from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.sisalto = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        if len(self.sisalto) == 0:
            return 0
        kpl = 0
        for ostos in self.sisalto:
            kpl += ostos.lukumaara()
        return kpl
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        if len(self.sisalto) == 0:
            return 0
        hinta = 0
        for ostos in self.sisalto:
            hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = Ostos(lisattava)
        for ostos_korissa in self.sisalto:
            if ostos_korissa.tuote == lisattava:
                ostos_korissa.muuta_lukumaaraa(1)
                break
        else:
            self.sisalto.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos_korissa in self.sisalto:
            if ostos_korissa.tuote == poistettava:
                ostos_korissa.muuta_lukumaaraa(-1)
            if ostos_korissa.lukumaara() == 0:
                self.sisalto.remove(ostos_korissa)
            
    def tyhjenna(self):
        self.sisalto = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.sisalto
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
