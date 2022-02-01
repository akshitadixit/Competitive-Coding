t = int(input())
while t > 0:
    t -= 1
    n, k = list(map(int, input().split()))
    s = [int(x) for x in input()]
    ctr = -1
    l = 0
    r = n-1
    while l <= r:
        mid = l+(r-l)//2
        temp = 0
        arr = s.copy()
        for i in range(mid, -1, -1):
            if (arr[i]+temp) % 10 == 0 or (i == mid and arr[i] == 0):
                continue
            else:
                arr[i] += temp
                arr[i] = arr[i] % 10
                temp += (10-arr[i])

                if temp > k:
                    r = mid-1
                    break

        if temp <= k:
            ctr = max(mid, ctr)
            l = mid+1

    print(ctr+1)
