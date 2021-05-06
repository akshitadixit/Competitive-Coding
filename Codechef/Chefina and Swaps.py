# cook your dish here
t = int(input())
while t>0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    flag = 0
    all_count = {} #all elements : their counts
    a_count = {} #elements of a : their counts
    b_count = {} #elements of b : their counts
    for x in a:
        if x in all_count:
            all_count[x] = all_count[x] +  1
        else:
            all_count[x] = 1
        if x in a_count:
            a_count[x] = a_count[x]  +  1
        else:
            a_count[x] = 1
    for y in b:
        if y in all_count:
            all_count[y] = all_count[y] +  1
        else:
            all_count[y] = 1
        if y in b_count:
            b_count[y] = b_count[y] +  1
        else:
            b_count[y] = 1
    for x in all_count:
        if (all_count[x]) % 2 == 1: #if a number occurs odd times => unidentical
            flag = 1
            break
    if flag == 1:
        print('-1')
    else:
        temp = {} #dictionary of all elements that need to be swapped
        for x in all_count:
            ca = 0
            cb = 0
            if x in a_count:
                ca = a_count[x]
            if x in b_count:
                cb = b_count[x]
            if(a_count != b_count):
                temp[x] = int(abs(ca - cb)/2) #the no. of swaps each requires

        if len(temp) == 0: #no element needs to be changed
            print(0)
        else:
            l = []
            for x in temp:
                for i in range(temp[x]):
                    l.append(x)
            l.sort()
            cost = 0
            m1 = min(all_count) #so that we can exchange with the min. element to minimise cost
            for i in range(int(len(l)/2)):
                if l[i] > m1*2:
                    cost = cost + m1*2
                else:
                    cost = cost + l[i]
            print(cost)
    t = t-1
    
    