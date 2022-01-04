'''
Given an array of intervals where intervals[i] = [starti, endi]
merge all overlapping intervals, and return an array of the
non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
'''

def merge_intervals(arr):
    i = 0
    while arr:
        if arr[i][1]<arr[i+1][1] or arr[i+1][0]<arr[i][1]:
            del arr[i]
            del arr[i+1]
            