def convert(s):
    
    new=list(s)
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    l = [values[i] for i in new]
    x = 0
    for i in range(len(l)):
        if i<len(l)-1 and l[i] < l[i+1]:
            x -= l[i]
        else:
            x += l[i]

    return x
    

print(convert("XC"))
print(convert("XXIX"))
print(convert("DCXCV"))