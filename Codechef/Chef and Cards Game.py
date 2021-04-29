# cook your dish here
t = int(input())
while t>0:
    n = int(input())
    c = 0
    m = 0
    while n>0:
        a, b = input().split()
        a = sum(int(digit) for digit in a)
        b = sum(int(digit) for digit in b)
        if a>b:
            c = c+1
        elif b>a:
            m = m+1
        else:
            c = c+1
            m = m+1
        n = n-1
    if c>m:
        print('0', c)
    elif m>c:
        print('1', m)
    else:
        print('2', c)
    t = t-1