import re

a = input()

if re.fullmatch(r'[A-Za-z0-9$#@]{6,16}', a):
    print("Podane hasło jest prawidłowe")
else:
    print("Hasło nie prawidłowe!")
