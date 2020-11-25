
a = int(input())
tabliczka = [[i*j for j in range(1,11)] for i in range(1,a+1)]

for elem in tabliczka:
  print(*elem)