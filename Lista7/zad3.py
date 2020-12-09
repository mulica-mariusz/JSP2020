import random, time

new1 = [random.randint(0,20) for _ in range(100)]
new2 = [random.randint(0,20) for _ in range(200)]
new3 = [random.randint(0,20) for _ in range(300)]

def bubble_sort(s):
    j = len(s)-1
    while j>=1:
        for i in range(j):
            if s[i] > s[i+1]:
                s[i],s[i+1] = s[i+1], s[i]
        j -= 1

    return s

start1=time.time()
bubble_sort(new1)
print(time.time()-start1)

start2=time.time()
bubble_sort(new2)
print(time.time()-start2)

start3=time.time()
bubble_sort(new3)
print(time.time()-start3)