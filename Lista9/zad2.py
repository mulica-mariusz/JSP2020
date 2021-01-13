import numpy as np
import sys
import io


filename = sys.argv[1]
try:
    f = open(filename, 'r')
    if isinstance(f, io.TextIOBase):
        n = []
        for line in f:
            n.append(float(line))

except IOError:
    x = [float(x) for x in sys.argv[1:]]
    print("Średnia: ",np.mean(x))
    print("Wariancja: ",np.var(x))
    print("Odchylenie standardowe: ", np.std(x))
else:
    print("Średnia: ",np.mean(n))
    print("Wariancja: ",np.var(n))
    print("Odchylenie standardowe: ", np.std(n))








