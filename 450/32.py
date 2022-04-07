'''
search element in sorted matrix
'''

import numpy as np


def search_optimal(arr, k):
    n = len(arr)
    m = len(arr[0])
    lo, hi = 0, m*n-1
    while lo <= hi:
        mid = (lo+hi)//2
        ele = arr[mid//m][mid % m]

        if ele == k:
            return True
        elif ele < k:
            lo = mid+1
        else:
            hi = mid-1
    return False


def search_Smart(arr, k):
    arr = list(np.array(arr).flatten())
    if k in arr:
        return True
    return False
    # or use binary search


print(search_Smart([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(search_optimal([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 16))
