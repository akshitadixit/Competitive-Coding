def jumps(arr):
    m = 0
    i = 0
    while i<len(arr)-1:
        if arr[i]==0:
            return -1
        i += arr[i]
        m += 1
    return m

a = list(map(int, input().split()))
print(jumps(a))