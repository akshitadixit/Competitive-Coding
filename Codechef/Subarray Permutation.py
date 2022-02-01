t = int(input())
while t > 0:
    t -= 1
    n, k = list(map(int, input().split()))
    arr = list(map(str, list(range(1, n+1))))
    if n != k:
        if k < 2:
            print(-1)
            continue
        k = k-2
        arr[k+1], arr[n-1] = arr[n-1], arr[k+1]
    print(' '.join(arr))
