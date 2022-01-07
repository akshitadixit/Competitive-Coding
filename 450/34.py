'''
Given a boolean 2D array of n x m dimensions where
each row is sorted. Find the 0-based index of the 
first row that has the maximum number of 1's.
'''


def max1(arr):
    mx = 0
    k = 0
    for i, x in enumerate(arr):
        if sum(x) > mx:
            mx = sum(x)
            k = i
    return k


arr = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
print(max1(arr))
