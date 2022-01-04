'''
Given an array Arr[] that contains N integers (may be positive, negative or zero).
Find the product of the maximum product subarray.
'''

from sys import maxsize
def max_prod(arr):
    mx = -maxsize-1
    prod = 1

    for x in arr:
        prod *= abs(x)
        if prod>mx:
            mx = prod
        if prod==0:
            prod = 1
    return mx

arr = list(map(int, input().split()))
print(max_prod(arr))