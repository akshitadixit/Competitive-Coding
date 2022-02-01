t = int(input())
while t > 0:
    t -= 1
    n, k = list(map(int, input().split()))
    s = [int(x) for x in input()]
    # print(s)
    ctr = 0
    for x in s:
        #print(x, k)
        if x == 0:
            ctr += 1
            continue
        if 10-x <= k:
            ctr += 1
            k = k - (10-x)
        else:
            break
    print(ctr)
