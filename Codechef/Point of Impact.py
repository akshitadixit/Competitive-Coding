t = int(input())
while t>0:
    n, k, x, y = list(map(int, input().split()))
    pts = []
    
    if x==y:
        print(n, n)
    else:
        if x<y:
            pts = [[n-abs(x-y), n],[n, n-abs(x-y)],[abs(x-y), 0],[0, abs(x-y)]]
        else:
            pts = [[n, n-abs(x-y)],[n-abs(x-y), n],[0, abs(x-y)],[abs(x-y), 0]]
        
        ans = pts[(k-1)%4]
        print(str(ans[0])+' '+str(ans[1]))
    
    t = t-1