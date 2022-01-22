import math
t = int(input())
while t > 0:
    n = int(input())
    flag = 0
    arr = list(map(int, input().split()))
    want = list(range(1, n+1))

    for x in arr:
        if x in want:
            del want[want.index(x)]
            continue
        while x > 0:
            x = int(math.floor(x/2))
            if x in want:
                del want[want.index(x)]
                break

        if x < 1:
            flag = 1
            break

    if flag == 0:
        print('YES')
    else:
        print('NO')
    t -= 1
