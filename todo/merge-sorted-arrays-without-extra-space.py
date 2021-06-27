'''
This approach does not maintain the sorted order
'''
def merge(a, b):
    i = j = 0
    print(max(a), min(b))
    while max(a)>min(b):
        p = a.index(max(a))
        q = b.index(min(b))
        if a[p]>b[q]:
            
            a[p], b[q] = b[q], a[p]
    return (a,b)

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(merge(a,b))