def union(a, b):
    # a and b are sorted arrays
    c = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i += 1
        elif b[j]<a[i]:
            c.append(b[j])
            j += 1
        else:
            c.append(b[j])
            i += 1
            j += 1

    while i<len(a):
        c.append(a[i])
        i += 1
    while j<len(b):
        c.append(b[j])
        j += 1
    
    return c

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(union(a,b))