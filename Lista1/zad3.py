import math

a = int(input())
b = int(input())
c = int(input())
p = 0.5 * a * b * math.sin(math.radians(c))
print(round(p, 2))