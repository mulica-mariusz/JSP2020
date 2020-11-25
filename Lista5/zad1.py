def convert(s):
    x = s.split()
    j = ["jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć", "dziesięć"] 
    k = ["jede", "dwa","trzy",  "czter", "pięt", "szes","siedem","osiem", "dziewięt"]
    n = ["naście"]
    d = ["dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt"]
    kn = [k1+n1 for k1 in k for n1 in n]
    if s in kn:
        print(kn.index(s)+11)
    elif s in j:
        print(j.index(s)+1)
    elif x[0] in d and x[1] in j:
        print((d.index(x[0])+2)*10+j.index(x[1])+1)
    else:
        print("Zły zapis słowny!")
    
    
word = input()
convert(word)