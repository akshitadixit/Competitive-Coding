'''
Pigeon-hole principle

'''
# print diff in sum of n-1 vs arr
# or use sign reversal

def dupli(arr):
    for x in arr:
        arr[abs(x)] = -arr[abs(x)]
        if arr[abs(x)]>0:
            return abs(x)

arr = list(map(int, input().split(',')))
print(dupli(arr))