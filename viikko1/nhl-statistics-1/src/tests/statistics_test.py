import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12), #16
            Player("Lemieux", "PIT", 45, 54), #99
            Player("Kurri",   "EDM", 37, 53), #90
            Player("Yzerman", "DET", 42, 56), # 98
            Player("Gretzky", "EDM", 35, 89) #124
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
        self.pelaaja = self.statistics.search("Semenko")
    def test_pelaajan_loytaminen(self):
        self.assertAlmostEqual(self.pelaaja.name, "Semenko")
    
    def test_palauttaa_tyhjan_jos_pelaajaa_ei_loydy(self):
        self.statistics.search("en_ole_olemassa")

    def test_palauttaa_pelaajan_pisteet(self):
        pisteet = self.statistics.sort_by_points(self.pelaaja)
        self.assertAlmostEqual(pisteet, 16)
    
    def test_loytaa_joukkueen_pelaajat(self):
        pelaajat = self.statistics.team("PIT")
        self.assertAlmostEqual(pelaajat[0].name, "Lemieux")
        self.assertAlmostEqual(len(pelaajat), 1)

    def test_top_scorers(self):
        top = self.statistics.top_scorers(5)
        self.assertAlmostEqual(top[0].name, "Gretzky")
        self.assertAlmostEqual(top[1].name, "Lemieux")
        self.assertAlmostEqual(top[2].name, "Yzerman")
        self.assertAlmostEqual(top[3].name, "Kurri")
        self.assertAlmostEqual(top[4].name, "Semenko")


