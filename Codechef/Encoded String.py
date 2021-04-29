pre = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
t = int(input())
while t>0:
    n = int(input())
    s = input()
    ans = ""
    for i in range(0,n-3,4):
        ans = ans + pre[int(s[i:i+4],2)]
    print(ans)
    t = t-1