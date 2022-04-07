'''
Merge 2 sorted arrays without extra space
'''


def merge_sorted(arr1, arr2):
    i, j = 0, 0
    m, n = len(arr1), len(arr2)
    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            print(arr1[i], end=' ')
            i += 1
        else:
            print(arr2[j], end=' ')
            j += 1
    if i < n:
        for x in range(i, n):
            print(arr1[x], end=' ')
    if j < m:
        for x in range(j, m):
            print(arr2[x], end=' ')


print(merge_sorted(list(map(int, input().split())),
      list(map(int, input().split()))))
