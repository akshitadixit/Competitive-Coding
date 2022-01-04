'''
merge 2 sorted arrays without using extra space
'''


def merge1(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i, j, k = 0, 0, n-1
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        else:
            arr2[j], arr1[k] = arr1[k], arr2[j]
            j += 1
            k -= 1
    return f'{sorted(arr1)}\n{sorted(arr2)}'


def merge2(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i, j = 0, 0


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(merge1(arr1, arr2))
