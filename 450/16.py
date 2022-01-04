'''
next greater permutation
if not possible then lowest possible perm.
replacement: in-place
memory: constant
'''

def nextperm(arr):
    if sorted(arr, reverse=True) == arr:
        return sorted(arr)
    for i in range(-1, -len(arr), -1):
        if arr[i]>arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            return arr

# weird ass