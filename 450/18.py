'''
Given an array of positive and negative numbers.
Find if there is a subarray (of size at-least one) with 0 sum.
'''

def zerosum(arr):
    sm, flag = 0, set()
    if 0 in arr:
        return 'Yes'
    for x in arr:
        sm += x
        if sm==0 or sm in flag:
            return 'Yes'
        flag.add(sm)
    return 'No'

arr = list(map(int, input().split()))
print(zerosum(arr))