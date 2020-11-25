def harmonic(n):
  s = 0
  for i in range(1,n+1):
    s += (1/i)
  return s

print(harmonic(66))
print(harmonic(2))