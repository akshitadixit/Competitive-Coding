s = input()
up = len([x for x in s if x.isupper()])
low = len([x for x in s if x.islower()])

if up>low:
	print(s.upper())
else:
	print(s.lower())