def maxsum(arr):
    max_sum = arr[0]
    sum = arr[0]

    for x in arr:
        sum += x
        if max_sum<sum:
            max_sum = sum

        if sum<0:
            sum = 0

    return max_sum

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print("Maximum contiguous sum is", maxsum(a))
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxsum(a))