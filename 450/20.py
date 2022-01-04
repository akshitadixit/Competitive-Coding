'''
no. of pairs of elements whose sum==k
'''

def givensum(arr, k):
    ctr = 0
    seen = set()
    for x in arr:
        if (x, k-x) not in seen and k-x in arr:
            ctr += 1
            seen.add((x, k-x))
    return ctr

arr = list(map(int, input().split()))
k = int(input())
print(givensum(arr, k))