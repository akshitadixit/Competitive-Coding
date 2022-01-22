a, n = list(map(int, input().split()))

from collections import deque

stak = deque().append(1)
x = n
ctr = 0
while x>1:
    if x%a:
        x = x//a
        ctr += 1
    else:
        x = int(str(x)[::-1])

print