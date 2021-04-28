# cook your dish here
t = int(input())
while t>0:
    n = int(input())
    l = list(map(int, input().split()))
    s = 0
    for i in range(0,n-1):
        s = s + abs(l[i+1]-l[i])-1
    print(s)
    t = t-1