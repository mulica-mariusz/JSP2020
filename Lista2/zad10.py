new_list = list(range(3,100,3))

del new_list[4::3]
print(round(sum(new_list)/len(new_list), 2))