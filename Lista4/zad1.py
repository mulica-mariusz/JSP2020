def nowa(lista):
  i=1
  s=0
  for x in lista:
    s += x
    i *= x
  return f"Iloczyn: {i} Suma: {s}"

print(nowa([8,3,2,6,9]))