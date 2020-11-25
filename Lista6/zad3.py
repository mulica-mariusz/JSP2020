def lookandsay(n):
    i = 0
    while i < n:
	    if i == 0:
		    look = [1]
	    else:
		    x = 1
		    new = []
		    for j in range(1, len(look)):
			    if look[j] == look[j - 1]:
				    x += 1
			    else:
				    new += [x, look[j - 1]]
				    x = 1
		    new += [x, look[len(look) - 1]]
		    look = new
	    i += 1
	    print(*look)
	
	 
   
n = int(input("Podaj liczbe wierszy: "))
lookandsay(n)


