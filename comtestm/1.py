t = int(input())
while t > 0:
    t -= 1
    n, l = list(map(int, input().split()))
    bin = [0]*32
    a = list(map(int, input().split()))
    for x in a:
        for j in range(l - 1, -1, -1):
            if x & 1:
                bin[j] += 1
            else:
                bin[j] -= 1
            x >>= 1

    ans = 0
    for i in range(l):
        ans <<= 1
        if bin[i] > 0:
            ans += 1
    print(ans)
 