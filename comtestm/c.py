from array import array

n, q = list(map(int, input().split()))
a = list(map(int, input().split()))

inds = {}
for i, x in enumerate(a):
    if x not in inds:
        inds[x] = array('i', [0, i+1])
    else:
        inds[x].append(i+1)

while q > 0:
    q -= 1
    x, k = list(map(int, input().split()))

    try:
        print(inds[x][k])
    except:
        print(-1)
