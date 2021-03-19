n = int(input())

def fun(s):
	while(len(set(str(s)))!=4):
		s = s+1
	return s

print(fun(n+1))