'''
Given an array (or string), the task is to reverse the array/string.
'''

def reverse_array(arr):
    start = 0
    end = len(arr)-1
    while start<end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

arr = list(map(int, input().split()))
print(reverse_array(arr))