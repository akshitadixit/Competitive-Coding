mat = []
i = [0,0]
for _ in range(5):
	mat.append(list(map(int, input().split())))

for x in mat:
	if 1 in x:
		i = [mat.index(x), x.index(1)]
		break

print(abs(2-i[0])+abs(2-i[1]))