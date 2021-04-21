# cook your dish here
from re import search
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ctr = 0
    flag = 0
    for x in s:
        if x=='*':
            ctr = ctr +1
            if ctr==k:
                flag = 1
                break
        else:
            ctr = 0
    if flag==1:
        print('YES')
    else:
        print('NO')