def pascal(n):
    lista = [[1]]
    for i in range(n):
        new_list = []
        new_list.append(lista[0][0])
        for j in range(len(lista)-1):
            new_list.append(lista[i][j]+lista[i][j+1])
        new_list.append(lista[-1][-1])
        lista.append(new_list)
    return lista

trojkat = pascal(5)
for elem in trojkat:
    print(*elem)