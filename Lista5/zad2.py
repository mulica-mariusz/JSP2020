def convert(w):
    s = ["sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset", "siedemset","osiemset","dziewięćset"]
    j = ["jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
    d = ["dziesięć", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"]
    t = ["jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście"]
    
    new = []
    l = [int(k) for k in list(str(w))]
    while True:
        if len(l)==4:
            l.pop(0)
            new.insert(0, "tysiąc")
        if len(l)==3:
            if l[0]==0:
                l.pop(0)
            else:
                new.append(s[l[0]-1])
                l.pop(0)
        if len(l)==2:
            if l[0]==1:
                if l[1]==0:
                    new.append(d[0])
                    l.pop(0)
                else:
                    new.append(t[l[1]-1])
                    l.pop(0)
            if l[0]==0:
                l.pop(0)
            else:
                new.append(d[l[0]-1])
                l.pop(0)
        if len(l)==1:
            if l[0]!=0:
                new.append(j[l[0]-1])
                l.pop(0)
        if len(l)==0:
            break
    print(" ".join(new))

 
convert(1110)
convert(1091)
convert(89)
