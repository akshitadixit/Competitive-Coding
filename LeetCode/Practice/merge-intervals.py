'''
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.

>>>> GRAPH QUESTION <<<<
'''

def merge(arr):
    arr = sorted(arr, key=lambda i: i[0])
    print(arr)
    res = []
    for x in arr:
        if res and x[0]<=res[-1][1]:
            res[-1][1] = max(x[1], res[-1][1])

        else:
            res.append(x)
    return res

arr = [[1,3],[2,6],[8,10],[15,18]]
print(merge(arr))