t = int(input())
while t > 0:
    a, b, c = list(map(int, input().split()))

    if 2*b == a+c:
        print('YES')
        t -= 1
        continue

    if 2*b < a+c:
        if a+c % b == 0 and b != 1:
            print('YES')
            t -= 1
            continue
        print('NO')

    if 2*b > a+c:
        if 2*b-max(a, c) % min(a, c) == 0:
            print("YES")
            t -= 1
            continue
        print('NO')

    t -= 1
