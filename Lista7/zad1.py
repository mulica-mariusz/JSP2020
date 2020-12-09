import time

def fibo1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo1(n-1)+fibo1(n-2)
    
def fibo2(n):
    i = 1
    a = 0
    b = 1
    while i < n:
        i += 1
        c = a+b
        a = b
        b = c  
    return b

start = time.time()
for i in range(25):
    fibo1(i)
print(time.time()-start)

start2= time.time()
for i in range(25):
    fibo2(i)
print(time.time()-start2)