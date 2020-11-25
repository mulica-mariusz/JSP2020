def delete_duplicates(lista):
    new = set(lista) ### druga opcja new=dict.fromkeys(lista)
    return list(new)

print(delete_duplicates([1,2,3,2,1,2,2,3,1,1,2]))
print(delete_duplicates(['a','b','e','b','a','e','a']))