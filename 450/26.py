'''
Given three arrays sorted in increasing order. 
Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
'''

def  set_method(a, b, c):
    seen = set()
    for x in a:
        if x not in seen:
            seen.add(x)
        else:
            print(x, end=' ')
    # repeat this for the other 2


def find_common(a, b, c):
    for x in a:
        if x in b and c:
            print(x, end=',')
    print('\b')

    return set(a).intersection(set(b).intersection(set(c)))


def traditional(a, b, c):
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] and a[i] == c[k]:
            print(a[i])
            print(i, j, k, b[j], c[k])
            i += 1
            j += 1
            k += 1
            continue

        m = min(a[i], b[j], c[k])
        if a[i] == m:
            i += 1
        elif b[j] == m:
            j += 1
        else:
            k += 1


A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]

#print(find_common(A, B, C))
print(traditional(A, B, C))
