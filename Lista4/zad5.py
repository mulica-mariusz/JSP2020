from itertools import permutations

def perm(lista):
    if len(lista)==len(set(lista)):
        for elem in permutations(lista):
            print(list(elem))
    else:
        for elem in set(permutations(lista)):
            print(list(elem))


perm([1,1,3])
perm([3,4,6])