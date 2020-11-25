from itertools import chain
new_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
print(list(chain.from_iterable(new_list)))