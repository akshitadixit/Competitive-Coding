n = int(input())
h = list(map(int, input().split()))
i = 0

while i <= n-2:
    if h[i+1] > h[i]:
        i += 1
    else:
        break

print(h[i])
