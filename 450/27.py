'''
Given an array of positive and negative numbers, 
arrange them in an alternate fashion such that every
positive number is followed by negative and vice-versa
maintaining the order of appearance. 

Number of positive and negative numbers need not be
equal. If there are more positive numbers they appear
at the end of the array. If there are more negative
numbers, they too appear in the end of the array.
'''


def alternate_signs(arr):
    # sort
    # find the dividing point
    # i = 0 and j = mid
    # swap until....?

    i, j, mid = 0, len(arr), 0
    arr.sort(reverse=True)
    while i < j:
        mid = (i+j)//2

        if arr[mid-1] >= 0 and arr[mid] < 0:
            break

        elif arr[mid] > 0:
            i = mid+1
        else:
            j = mid-1

    # now mid has the first -ve
    i = 1
    j = mid

    while i < j and j < len(arr):
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
        i += 2

    return arr


arr = [-5, 3, 4, 5, -6, -2, 8, 9, -1, -4]
arr = [-22, 3, 4, -1]
arr = [2, 3, -4, -1, 6, -9]
# sorted = 4, 3, -1, -2
print(alternate_signs(arr))
