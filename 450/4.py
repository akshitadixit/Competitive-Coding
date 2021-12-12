'''
Find k-th min element in an unsorted array
'''

# we use a ordered map approach here, a better approach is via min and max heaps or "QUICK SELECT"

from collections import OrderedDict

def find_kth_min(arr, k):
    od = OrderedDict()
    for x in sorted(arr):
        od[x] = arr.count(x)
    
    sum = 0
    for x in od:
        sum += od[x]
        if sum>=k:
            print(od)
            return x

    return -1

arr = list(map(int, input().split()))
print(find_kth_min(arr, 4))