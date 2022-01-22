import math
n, k = list(map(int, input().split()))


dist = lambda p, q: math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)


x, y = [0]*n, [0]*n
res = []

for i in range(n):
    x[i], y[i] = list(map(int, input().split()))
    for j in range(i):
        if dist([x[i], y[i]], [x[j], y[j]]) <= k:
            res.append([x[i], y[i]])
            res.append([x[j], y[j]])

print(len(res))
for x in res:
    print(x[0], x[1])
