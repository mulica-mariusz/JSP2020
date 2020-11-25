from trojkat import *
a = int(input())
b = int(input())
c = int(input())
new = [a+b>c, b+c>a, c+a>b]
if all(new):
    print("Pole: ", pole(a,b,c))
    print("Obwód: ", obwod(a,b,c))
    boki(a,b,c)
    katy(a,b,c)
else:
    print("Z podanych długości boków nie można utworzyć trójkąta")