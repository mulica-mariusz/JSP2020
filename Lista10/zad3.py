from itertools import combinations, chain 

class Comb:

    def __init__(self, l):
        self.l = l

    def sublists(self):
        new = chain(combinations(self.l, 3))
        suma = 0
        result = []
        for elems in new:
            for el in elems:
                suma += el
            if suma == 0:
                result.append(list(elems))
            suma *= 0
        return result
        
        
    

com = Comb([5,-4,1,3,-1,-2,-8])
print(com.sublists())