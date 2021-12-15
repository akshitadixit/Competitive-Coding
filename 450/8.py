'''
Given an array, rotate the array by k positions in clock-wise direction.
'''

def shiftbyk_clock(arr, k):
    # (i+k)%n
    return [arr[(i+k)%len(arr)] for i in range(len(arr))]

def shiftbyk_anticlock(arr, k):
    # (i-k)%n
    return [arr[(i-k)%len(arr)] for i in range(len(arr))]

arr = list(map(int, input().split()))
print(shiftbyk_clock(arr, 2))
print(shiftbyk_anticlock(arr, 2))