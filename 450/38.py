'''
find indexes of first and last 
occurrences of an element x in the given array.
'''


def findindices(arr, x):
    beg, end = 0, len(arr)-1
    mid = 0
    i1, i2 = -1, -1

    while beg < end:
        mid = (beg+end)//2
        if arr[mid] >= x:
            end = mid
        elif arr[mid] < x:
            beg = mid+1

    i1 = mid

    beg, end = 0, len(arr)-1
    mid = 0

    while beg < end:
        mid = (beg+end)//2
        if arr[mid] >= x:
            end = mid
        elif arr[mid] < x:
            beg = mid+1
