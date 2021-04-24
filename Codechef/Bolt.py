# cook your dish here
for _ in range(int(input())):
    k1, k2, k3, v = map(float, input().split())
    if round(100/(k1*k2*k3*v), 2) < 9.58:
        print("YES")
    else:
        print("NO")