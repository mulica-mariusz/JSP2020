def nwd(a,b):
    nw = 0
    while True:
        if a%b==0:
            nw = b
            break
        else:
            c=a
            a=b
            b=c%b   
    return nw

print(nwd(256,12))
print(nwd(144,12))
