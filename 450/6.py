'''
Move all negative numbers to beginning and positive to end with constant extra space
An array contains both positive and negative numbers in random order.
Rearrange the array elements so that all negative numbers appear before all positive numbers.
'''

def sort_np_preferred(arr):
    # partition process of quicksort
    j = 0
    for i in range(1, len(arr)):
        if arr[i]<0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

def sort_np1(arr):
    # two pointer solution
    left = 0
    right = len(arr)-1
    while left<=right:
        if arr[left]<0 and arr[right]<0:
            left += 1
        elif arr[left]>0 and arr[right]>0:
            right -= 1
        elif arr[left]>0 and arr[right]<0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        else:
            left += 1
            right -=1
    return arr

def sort_np2(arr):
    # doesn't deal with zeros
    lo = 0
    mid = 0
    hi = len(arr)-1
    while mid<=hi:
        if arr[mid]<0:
            arr[lo], arr[mid] = arr[mid], arr[mid]
            lo += 1
            mid+=1
        elif arr[mid] == 0:
            mid += 1
        elif arr:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
    return arr

arr = list(map(int, input().split()))
''' -12, 11, -13, -5, 6, -7, 5, -3, -6 0 '''
print(sort_np2(arr))
print(sort_np1(arr))
print(sort_np_preferred(arr))