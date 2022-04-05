'''
search an element in a matrix with foll properties:
- each row is sorted
- first ele of each row > last ele of prev row
'''


def search_matrix(arr, k):
    n = len(arr[0])
    beg, end = 0, len(arr)*len(arr[0])-1
    while beg <= end:
        mid = (beg+end)//2
        ele = arr[mid//n][mid % n]

        if ele < k:
            beg = mid+1
        elif ele > k:
            end = mid-1
        else:
            return [mid//n, mid % n]
    return -1


arr = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
print(search_matrix(arr, 1))
