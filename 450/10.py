'''
Given an array arr[] denoting heights of N towers and a positive integer K,
you have to modify the height of each tower either by increasing or decreasing
them by K only once. After modifying, height should be a non-negative integer. 
Find out what could be the possible minimum difference of the height of
shortest and longest towers after you have modified each tower.

Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as {3, 3, 6, 8}.
The difference between the largest and the smallest is 8-3 = 5.
'''

def max_height_diff(arr, k):
    return max(arr) - min (arr) - 2*k

arr = list(map(int, input().split()))
print(max_height_diff(arr, 3))