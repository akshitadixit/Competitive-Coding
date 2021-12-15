'''
Kadane's algo:

Given an array Arr[] of N integers.
Find the contiguous sub-array(containing at least one number)
which has the maximum sum and return its sum.
'''

from sys import maxsize

def sum_maxsubarr(arr):
    max_so_far = -maxsize-1
    max_till_here = 0

    start, end = 0, 0
    k = 0

    for i, x in enumerate(arr):
        max_till_here += x
        if max_till_here>max_so_far:
            max_so_far = max_till_here
            start = k
            end = i
        if max_till_here<0:
            max_till_here=0
            k = i+1
    return arr[start:end+1]

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sum_maxsubarr(a))