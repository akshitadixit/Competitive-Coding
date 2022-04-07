'''
Given two arrays: a1[0..n-1] of size n and a2[0..m-1]
of size m. Task is to check whether a2[] is a subset of
a1[] or not. Both the arrays can be sorted or unsorted. It may be assumed that elements in both array are distinct.
'''

def subset_hashtable(arr1, arr2):
    # time = m+n
    # space = m
    pass

def check_subset(arr1, arr2):
    # O(n) time and O(1) space
    for x in arr2:
        if x not in arr1:
            return False
    return True


def traditional(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i, j = 0, 0
    while j < len(arr2):
        # if the smallest ele of leftover arr2 not in leftover arr1 then FALSE
        if arr2[j] < arr1[i]:
            print(arr1, arr2, i, j)
            return False
        elif arr2[j] > arr1[i]:
            i += 1
        else:
            i += 1
            j += 1
    return True


a = [10, 5, 2, 23, 19]
b = [11, 3, 7, 1]

print(traditional(a, b), 'v/s', check_subset(a, b))
