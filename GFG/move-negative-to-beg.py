'''
An array contains both positive and negative numbers in random order. 
Rearrange the array elements so that all negative numbers appear before all positive numbers.

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
'''

def move(arr):
    l = 0
    r = len(arr) - 1
    while l<=r:
        if arr[l]<0:
            l = l+1
        elif arr[l]>=0 and arr[r]<0:
            arr[l], arr[r] = arr[r], arr[l]
            l = l+1
            r = r-1
        else:
            r = r-1
    return arr

import time
arr = list(map(int, input().split()))
t0 = time.time()
print(move(arr))
t1 = time.time()
print(t1-t0)