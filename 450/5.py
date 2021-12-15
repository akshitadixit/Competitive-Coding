'''
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

Sort the array in-place.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''

# 0-lo = zeroes
# lo-mid = ones
# mid-hi = unknown
# hi-end = 2

def sort_012(arr):
    hi = len(arr) -1
    lo = 0
    mid = 0
    while mid<=hi:
        if arr[mid] == 0:
            arr[mid], arr[lo] = arr[lo], arr[mid]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
    return arr

arr = list(map(int, input().split()))
print(sort_012(arr))