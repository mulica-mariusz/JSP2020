from itertools import combinations, chain 

class Comb:

    def __init__(self, l):
        self.l = l

    def sublists(self):
        new = chain(*map(lambda x: combinations(self.l, x), range(0, len(self.l)+1)))
        return [list(el) for el in new]
        
    

com = Comb([5,4,3])
print(com.sublists())