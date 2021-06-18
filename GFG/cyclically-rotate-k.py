def rotate(arr, k):
    # (i+k)%len(arr)
    l = len(arr)
    for i in range(l):
        print(arr[(i+k)%l], end=" ")

arr = list(map(int, input().split()))
k = int(input())
rotate(arr, k)