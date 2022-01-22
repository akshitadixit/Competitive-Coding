n, k = list(map(int, input().split()))
p = list(map(int, input().split()))

for i in range(k, n+1):
    res = sorted(p[:i], reverse=True)[k-1]
    print(res)
