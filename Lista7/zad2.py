import random, time

new1 = [random.randint(0,20) for _ in range(100)]
new2 = [random.randint(0,20) for _ in range(200)]
new3 = [random.randint(0,20) for _ in range(300)]

def insert_sort(s):
    
    for i in range(len(s)):
        key = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > key):
            s[j+1] = s[j]
            s[j] = key
            j -= 1
        
    return s
start1=time.time()
insert_sort(new1)
print(time.time()-start1)

start2=time.time()
insert_sort(new2)
print(time.time()-start2)

start3=time.time()
insert_sort(new3)
print(time.time()-start3)