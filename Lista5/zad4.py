def convert(s, k="sz"):
    klucz1 = {"a" : "y", "e" : "i", "i" : "o", "o" : "a", "y" : "e"}
    klucz2 = {"y" : "a", "i" : "e", "o" : "i", "a" : "o", "e" : "y"}
    new = []
    if k == "sz":
        klucz = klucz1
    elif k == "de":
        klucz = klucz2
    x= [char for char in s]
    for k in x:
        if k in klucz:
            new.append(klucz[k])
        else:
            new.append(k)
    print("".join(new))
    

convert('to jest moj tekst', 'sz')
convert('ta jist maj tikst', 'de')
convert('jeden dwa trzy')
convert('jidin dwy trze', 'de')