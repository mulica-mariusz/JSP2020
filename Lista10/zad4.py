import xml.etree.ElementTree as ET
import math

class Kursy():
    def __init__(self, xml_filename):
        self.tree = ET.parse(xml_filename)
        self.root = self.tree.getroot()

    def lista_kursy(self):
        print('Dostępne kursy:')
        for kurs,kod,przel in zip(self.root.iter('kurs_sredni'), self.root.iter('kod_waluty'), self.root.iter('przelicznik')):
            print(przel.text, kod.text, ":", kurs.text, "zł")
    
    def kon_PLN(self, waluta, wartosc):
        for kurs,kod,przel in zip(self.root.iter('kurs_sredni'), self.root.iter('kod_waluty'), self.root.iter('przelicznik')):
            if waluta == kod.text:
                print(wartosc, waluta, "=> ", float(kurs.text)*wartosc/int(przel.text), "PLN")
                print(wartosc, "PLN =>", waluta, int(przel.text)*wartosc/float(kurs.text))
            else:
                continue
    
    def kon_walut(self, wal1, wal2, war1):
        for kurs,kod,przel in zip(self.root.iter('kurs_sredni'), self.root.iter('kod_waluty'), self.root.iter('przelicznik')):
            if wal1 == kod.text:
                kurs1 = float(kurs.text)
                przel1 = int(przel.text)
                
            elif wal2 == kod.text:
                kurs2 = float(kurs.text)
                przel2 = int(przel.text)
        print(war1, wal1, "=>",round(przel2*(kurs1*war1/przel1)/kurs2,2), wal2)

try:
    kursy=Kursy('kursy.xml')
except IOError:
    print("Błąd przy wczytywaniu pliku")
else:
    kursy.lista_kursy()
    waluta=input('Konwersja PLN <=> Wybrana waluta. Podaj walutę: ')
    wartosc=int(input("Podaj kwotę: "))
    kursy.kon_PLN(waluta, wartosc)
    waluta1=input('Podaj posiadaną walutę: ')
    wartosc1=int(input("Podaj posiadaną kwotę: "))
    waluta2=input('Podaj walutę, na która chcesz zamienić: ')
    kursy.kon_walut(waluta1, waluta2, wartosc1)