from SzyfrCezara import decode,encode
import datetime
import os.path
from os import path
from pathlib import Path

dire_path = input('Podaj ścieżkę do katalogu, w którym są pliki do odszyfrowania: ')
new = datetime.datetime.now()
try:
    if len(os.listdir(dire_path)) == 0:
        print("Brak plików w danym katalogu")
    else:
        for filename in os.listdir(dire_path):
            if filename.startswith("plik_zaszyfrowany"):
                n = filename[17]
                f = open(os.path.join(dire_path,filename),'r')
                dire = dire_path + f"\\plik_deszyfrowany{n}_{new.year}_{new.month}_{new.day}.txt"
                g = open(dire, "w")
                while True:
                    line = f.readline().strip()
                    g.write(decode("".join(line),int(n)))
                    g.write("\n")
                    if not line:
                        break
                g.close()
except FileNotFoundError:
    print("Podany katalog nie istnieje")

except PermissionError:
    print("Brak uprawnień do podanego katalogu")
except IOError:
    print("Napotkano niespodziewany błąd. Spróbuj ponownie")