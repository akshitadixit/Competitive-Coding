'''
median in row-wise sorted matrix

binary-search -> monotonically increasing search-space
'''


def numbersLessThan(val, arr):
    ctr = 0
    for a in arr:
        lo, hi = 0, len(a)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if a[mid] <= val:
                lo = mid+1
            else:
                hi = mid-1
        ctr += lo
    return ctr


def median(arr):
    # median is any value for which
    # the no. of values <= it are > (n*m)//2

    lo, hi = 1, 10**9
    half = (len(arr)*len(arr[0]))//2  # (n*m)//2
    while lo <= hi:
        mid = (lo+hi)//2
        if numbersLessThan(mid, arr) <= half:
            lo = mid+1
        else:
            hi = mid-1

    return lo


n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

print(median(arr))
