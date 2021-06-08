import time

a = [x for x in range(1, 1000000)]
t0 = time.time()
a.reverse()
t1 = time.time()
print(t1 - t0)
t1 = time.time()
a = a[::-1]
t2 = time.time()
print(t2-t1)