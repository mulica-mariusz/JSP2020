a = int(input())
b = int(input())

if b>a:
    x=b
    b=a
    a=x

z = a % b
z *= 3
print(z)