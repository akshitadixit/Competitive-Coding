k = int(input())

maps = {1: 2, 2: 20, 3: 22}

ans = bin(k).replace("0b", "")
ans = ans.replace('1', '2')
ans = ans.lstrip('0')

print(ans)
 