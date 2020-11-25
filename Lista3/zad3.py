import math
a = int(input())
b = int(input())
c = int(input())

if a!=0:
  delta=(b**2)-4*a*c
  if delta<0:
    print("Brak rozwiązań rzeczywistych")
  elif delta==0:
    x12=-b/(2*a)
    print("Jedno rozwiązanie: x=",x12)
  elif delta>0:
    x1= (-b-math.sqrt(delta))/(2*a)
    x2= (-b+math.sqrt(delta))/(2*a)
    print("Dwa rozwiązania: x1=",x1,"oraz x2=",x2)

else:
  print("Współczynnik a nie może wynosić 0.")