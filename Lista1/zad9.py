import cmath, math

z = complex(input())
print("Moduł: ", round(abs(z),3))
print("Argument: ", round(math.degrees(cmath.phase(z)),2))
print("Sprzężenie: ", z.conjugate())