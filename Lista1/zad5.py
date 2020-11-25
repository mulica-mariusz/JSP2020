# math.floor(x) - python zwraca największą liczbę całkowitą nie większa niż x np. math.floor(31.78) = 31
# round(x, y) - zwraca zaokrąglenie liczby gdzie y oznacza liczbę miejsc po przecinku. Domyślnie y=0,
# wtedy zwraca liczbe całkowitą na zasadach jak w matematyce np. round(31.78) = 32
# // zwraca największa liczbę całkowitą nie większa niż wynik dzielenia np (5//2) = 2 

import math

print(round(7/3))
print(round(7/3, 2))
print(math.floor(7/3))
print(7 // 3)
