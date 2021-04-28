for _ in range(int(input())):
    n, x, k = map(int, input().split())
    n = n + 1
    if x / k != int(x / k):
        if (n+1)/k != int((n+1)/k):
            print("NO")
    else:
        print("YES")