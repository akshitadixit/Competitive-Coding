t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n):
        a[i], b[i] = max(a[i], b[i]), min(a[i], b[i])

    print(max(a)*max(b))


# 2 9 3 5 2 2 -> 9 8 5 5 4 3
# 3 8 5 4 0 1 -> 3 2 2 2 1 0

# 3 2 3 2 2 2 ->
# 1 4 6 5 1 5 ->
