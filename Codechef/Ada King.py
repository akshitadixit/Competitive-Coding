# cook your dish here
t = int(input())
while t>0:
    k = int(input())
    flag = 0
    ch = '.'
    for i in range(0,8):
        for j in range(0,8):
            if k>0:
                k = k-1
            elif k==0 and flag<9:
                ch = 'X'
                flag = flag + 1
            else:
                ch = '.'
            if i==0 and j==0:
                print('O', end='')
            else:
                print(ch, end='')
        print('\n')
    print('\n')
    t = t-1