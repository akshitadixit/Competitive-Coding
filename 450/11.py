'''
Your task is to complete function minJumps() which takes
the array arr and it's size N as input parameters and
returns the minimum number of jumps. If not possible returns -1.
'''

def jumps(arr):
    i = 0
    ctr = 0
    while i<len(arr)-1:
        x = arr[i]
        if x==0:
            return -1
        i += x
        ctr += 1
    return ctr

arr = list(map(int, input().split()))
print(jumps(arr))