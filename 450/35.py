'''
Find the length of the longest sub-sequence such that
elements in the subsequence are consecutive integers,
the consecutive numbers can be in any order. All +ve integers.
'''


def longest_subseq(arr):
    arr.sort()
    arr = list(set(arr))
    beg, mid, end = 0, 0, len(arr)-1
    ctr = 0
    while beg <= end:
        mid = (beg+end)//2
        print(arr, arr[mid])

        if mid < end:
            if arr[mid-1]+1 == arr[mid] and arr[mid+1]-1 == arr[mid]:
                beg = mid+1
                ctr = mid

            else:
                ctr = mid+1
                break

        else:
            if arr[mid] == arr[mid-1]+1:
                beg = mid+1
                ctr = beg

    return ctr


arr = [2, 6, 1, 9, 4, 5, 3]
print(longest_subseq(arr))
