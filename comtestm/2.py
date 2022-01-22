from array import array
t = int(input())


while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    flag = 1

    maps = {}
    listmap = array('i', [])
    ans = n+1
    for i in range(n):
        x = a[i]
        listmap.append(x)
        if listmap.index(x) != len(listmap)-1:
            ans = min(ans, i-maps[x])

        maps[x] = i

    print(n-ans)
