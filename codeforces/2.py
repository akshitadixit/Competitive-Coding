t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))

    ref = a[-1]
    ctr = 0
    i = 1
    j = n-2
    while j > -1:
        while j > -1 and a[j] == ref:
            i += 1
            j -= 1
        if j < 0:
            break
        ctr += 1
        j = j-i
        i *= 2

    print(ctr)
