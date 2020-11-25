a = input()

x = a.replace(a[0], "$")
print(x.replace(x[0], a[0], 1))