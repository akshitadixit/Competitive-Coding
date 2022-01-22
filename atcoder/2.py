import math
n = int(input())
x, y = [0]*n, [0]*n


def dist(x, y): return math.sqrt(x*x + y*y)


mx = -1

for i in range(n):
    x[i], y[i] = list(map(int, input().split()))
    for j in range(i):
        mx = max(mx, dist(x[i]-x[j], y[i]-y[j]))

print(mx)
