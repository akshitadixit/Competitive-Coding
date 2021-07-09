'''
Proving that at least one duplicate must exist in nums
is an application of the pigeonhole principle.
Here, each number in nums is a "pigeon" and each distinct number
that can appear in nums is a "pigeonhole". Because there are n+1
numbers and n distinct possible numbers, the pigeonhole principle
implies that if you were to put each of the n+1 pigeons into n pigeonholes,
at least one of the pigeonholes would have 2 or more pigeons.
'''

def find(arr):
    d = {}
    for x in arr:
        if d.get(x):
            return x
        d[x] = 1
    return 0

from collections import Counter
def find2(arr):
    c = Counter(arr)
    return (c.most_common()[0][0])

def find3(arr):
    '''
    since array contains all +ve nos from 1 to n
    we change the sign of the number at the a[i]th index
    and if the ith index is already -ve then we have our duplicate a[i]
    '''
    for i in range(len(arr)):
        if arr[abs(arr[i])]<0:
            print(arr)
            return abs(arr[abs(arr[i])])
        arr[arr[i]] *= -1

    return -1

#arr = list(map(int, input().split()))
ar = [ 1, 5 , 8, 7, 6, 2, 3, 4, 7]
print(find3(ar))
