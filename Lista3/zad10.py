def parzysta(i):
  return all([int(cyfra)%2==0 for cyfra in str(i)])

new_list = [i for i in range(100,401) if parzysta(i)]
print(new_list)