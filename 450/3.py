'''
Find the min and max elements in the array (not a python question)
'''

def find_min_max(arr):
    n = len(arr)
    mx, mn = 0, 0
    i = 0
    if n%2==0:
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        i = 2
    else:
        mx = mn = arr[0]
        i = 1

    while i<n-1:
        if arr[i]<arr[i+1]:
            mx = max(mx, arr[i+1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i+1])

        i += 1

    return (mx, mn)

arr = list(map(int, input().split()))
print(find_min_max(arr))