'''
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
'''

def max_profit(arr):
    # fails 
    # arr = [2,4,1]
    # correct ans = 2, o/p = 0
    mn = min(arr)
    mx = max(arr[arr.index(mn):])
    return mx-mn

from sys import maxsize
def alternate(arr):
    mx = 0
    mn = maxsize
    for x in arr:
        if x<mn:
            mn = x
        elif x-mn>mx:
            mx = x-mn
    return mx

arr = list(map(int, input().split()))
print(max_profit(arr))
print(alternate(arr))