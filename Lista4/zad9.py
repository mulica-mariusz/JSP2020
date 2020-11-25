def silnia(n):
  s = 1
  for i in range(1, n+1):
    s *= i
  return s

print(silnia(5))
print(silnia(10))