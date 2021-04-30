t = int(input())
while t>0:
    n = int(input())
    set_x = {}
    set_y = {}
    for i in range(4*n - 1):
        a = tuple(map(int, input().split()))
        if a[1] in set_y:
            set_y[a[1]] = set_y[a[1]] +  1
        else:
            set_y[a[1]] = 1
        if a[0] in set_x:
            set_x[a[0]] = set_x[a[0]] +  1
        else:
            set_x[a[0]] = 1
    fin = []
    for i in set_x:
        if set_x[i]%2==1:
            fin.append(i)
            break
    for j in set_y:
        if set_y[j]%2==1:
            fin.append(j)
            break
    print(fin[0], fin[1])
    t = t-1
