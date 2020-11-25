a = int(input())

if (a%2==0):
    print("Parzysta")
else:
    print("Nieparzysta")

new_list = ["parzysta", "nieparzysta"]
print(new_list[a%2])