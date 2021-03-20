n = input()

l = len([x for x in n if x in '47'])

if l==4 or l==7:
	print("YES")
else:
	print("NO")