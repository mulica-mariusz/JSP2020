import math
def obwod(a,b,c):
    return a+b+c

def pole(a,b,c):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return round(s,2)

def boki(a,b,c):
    new = [a==b,b==c,c==a]
    if all(new):
        print("Trójkąt jest równoboczny")
    elif any(new):
        print("Trójkąt jest równoramienny")
    else:
        print("Trójkąt jest różnoboczny")


def katy(a,b,c):
    y=math.acos((b**2+c**2-a**2)/(2*b*c))
    x=math.acos((a**2+b**2-c**2)/(2*a*b))
    z=math.acos((a**2+c**2-b**2)/(2*a*c))

    if round(math.degrees(y),2) < 90 and round(math.degrees(x),2) < 90 and round(math.degrees(z),2) < 90:
        print("Trójkąt jest ostrokątny")       
    if round(math.degrees(y)) == 90 or round(math.degrees(x)) == 90 or round(math.degrees(z)) == 90:
        print("Trójkąt jest prostokątny")
    if math.degrees(y) > 90 or math.degrees(x) > 90 or math.degrees(z) > 90:
        print("Trójkąt jest rozwartokątny")
    

