t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    print(max(arr)-min(arr))
    t -= 1
