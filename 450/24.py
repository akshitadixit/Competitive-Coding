'''
print max no. of consecutive ones in a binary array (unsorted)
'''


def max1s(arr):
    mx = 0
    sum = 0
    for x in arr:
        if x == 0:
            sum = 0
        else:
            sum += 1

        mx = max(sum, mx)
    return mx


arr = [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0]
print(max1s(arr))
