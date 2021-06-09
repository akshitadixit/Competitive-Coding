import time

def sort_func(arr):
    lo, mid = 0, 0
    hi = len(arr) - 1
    while mid<=hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo = lo + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid+1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi = hi-1
    return arr

def counting_sort(arr):
    c0 = c1 = c2 = 0
    for x in arr:
        if x == 0:
            c0 += 1
        elif x == 1:
            c1 += 1
        else:
            c2 += 1

    return [0]*c0 + [1]*c1 + [2]*c2

arr = list(map(int, input().split()))
t0 = time.time()
print(sort_func(arr))
t1 = time.time()
print(counting_sort(arr))
t2 = time.time()
print(t1-t0)
print(t2-t1)