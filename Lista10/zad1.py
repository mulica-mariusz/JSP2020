import math
class Kolo:
    def __init__(self, r):
        self.r = r

    def pole(self):
        return round(self.r**2 * math.pi, 2)

    def obwod(self):
        return round(self.r * 2 * math.pi, 2)

kolko = Kolo(5)
print("Obwód:",kolko.obwod(), " Pole:",kolko.pole())