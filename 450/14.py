'''
Kadane's algo - max contiguous sum
'''

from sys import maxsize

def kadane(arr):
    mx = -maxsize-1
    sum = 0
    for x in arr:
        sum += x
        if sum>mx:
            mx = sum
        if sum<0:
            sum = 0

    return mx

arr = list(map(int, input().split()))
print(kadane(arr))