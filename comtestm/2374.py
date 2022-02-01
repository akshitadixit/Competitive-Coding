from collections import deque


n = int(input())
s = input()

ans = deque([n])
for i in range(n - 1, -1, -1):
    if s[i] == 'R':
        ans.appendleft(i)
    else:
        ans.append(i)

print(' '.join([str(x) for x in ans]))
