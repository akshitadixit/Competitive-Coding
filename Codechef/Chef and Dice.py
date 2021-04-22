t = int(input())
for i in range(t):
    n = int(input())
    dc = int(n/4)
    td = n%4
    if(td == 0):
        dc -= 1
        td += 4
    dc1 = 0
    m = 0
    if(td<4 and dc>=1):
        m = 4-td
        dc -= 1 
        dc1 = 1
    t1 = {0:0, 1:48, 2:52, 3:56}
        
    bot = 44
    t2 = {1:20, 2:36, 3:51, 4:60}
    y = 0
    x = t2.get(td)
    y = dc*bot
    z = dc1*t1.get(m)
    v = x+y+z
    print(v)