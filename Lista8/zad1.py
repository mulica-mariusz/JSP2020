from SzyfrCezara import decode,encode
import datetime
import os.path
from os import path
from pathlib import Path

file_path = input('Podaj ścieżkę do pliku, który chcesz zaszyfrować: ')
n = input('Podaj liczbę o jaką chcesz dokonać szyfrowania (1-10): ')
new = datetime.datetime.now()
dire_path = input('Podaj scieżkę do katalogu, w którym chcesz zapisać zaszyfrowany plik: ')
dire = dire_path + f"\\plik_zaszyfrowany{n}_{new.year}_{new.month}_{new.day}.txt"

try:
    os.makedirs(dire_path)
except FileExistsError:
    pass
except PermissionError:
    print("Nie można zapisać pliku do danej ścieżki - brak uprawnień")
except IOError:
    print("Napotkano jakiś niespodziewany problem")

if os.path.exists(dire_path):
    try:
        f = open(file_path, 'r')
        g = open(dire, "w")
        while True:
            line = f.readline().strip()
            g.write(encode("".join(line),int(n)))
            g.write("\n")
            if not line:
                break
        g.close()
    except FileNotFoundError:
        print("Plik, który chciałeś zaszyfrować nie istnieje!") 
    except ValueError:
        print("Zamiast liczby 1-10 podano inny znak!")
