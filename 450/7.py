'''
Given two arrays a[] and b[] of size n and m respectively.
The task is to find union and intersection between these two arrays.
Expected Time Complexity : O((n+m)log(n+m))
Expected Auxilliary Space : O(n+m)
'''

def union(arr1, arr2):
    n = len(arr1)-1
    m = len(arr2)-1
    res = []
    i, j = 0, 0
    while i<=n:
        if arr1[i] not in res:
            res.append(arr1[i])
        i+=1
    while j<=m:
        if arr2[j] not in res:
            res.append(arr2[j])
        j += 1
    return res

def intersection(arr1, arr2):
    n = len(arr1)-1
    i = 0
    res = []
    while i<=n:
        if arr1[i] in arr2 and arr1[i] not in res:
            res.append(arr1[i])
        i += 1

    return res

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(union(arr1,arr2))
print(intersection(arr1, arr2))

print(set(arr1).union(set(arr2)))
print(set(arr1).intersection(set(arr2)))