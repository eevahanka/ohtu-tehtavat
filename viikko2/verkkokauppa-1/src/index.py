from kauppa import Kauppa
from pankki import pankki as default_pankki
from varasto import varasto as default_varasto
from viitegeneraattori import viitegeneraattori as default_viitegeneraattori
from kirjanpito import kirjanpito as default_kirjanpito

def main():
    viitegeneraattori = default_viitegeneraattori
    kirjanpito = default_kirjanpito
    varasto = default_varasto
    pankki = default_pankki
    kauppa = Kauppa()

    # kauppa hoitaa yhden asiakkaan kerrallaan seuraavaan tapaan:
    kauppa.aloita_asiointi()
    kauppa.lisaa_koriin(1)
    kauppa.lisaa_koriin(3)
    kauppa.lisaa_koriin(3)
    kauppa.poista_korista(1)
    kauppa.tilimaksu("Pekka Mikkola", "1234-12345")

    # seuraava asiakas
    kauppa.aloita_asiointi()

    for _ in range(0, 24):
        kauppa.lisaa_koriin(5)

    kauppa.tilimaksu("Arto Vihavainen", "3425-1652")

    # kirjanpito
    print(kirjanpito.tapahtumat)
    for tapahtuma in kirjanpito.tapahtumat:
        print(tapahtuma)


if __name__ == "__main__":
    main()
