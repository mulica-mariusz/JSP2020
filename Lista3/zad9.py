m = int(input())
n = int(input())
tablica = [[i*j for j in range(1,n+1)] for i in range(1,m+1)]

for elem in tablica:
  print(*elem)