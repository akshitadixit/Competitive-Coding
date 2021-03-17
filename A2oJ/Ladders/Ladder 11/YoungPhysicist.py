n = int(input())
x = 0
y = 0
z = 0
for _ in range(n):
    p, q, r = map(int, input().split())
    x += p
    y += q
    z +=r
if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")
