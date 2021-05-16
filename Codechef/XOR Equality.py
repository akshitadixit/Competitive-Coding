m = 1000000007 #the modulo
def ans(x, n):
    a = 1
    x = x % m

    if x == 0:
        return 0
        
	# check if n is odd then multiply x with result
    while n > 0:
        if ((n & 1) == 1):
            a = (a * x) % m
		# n to be even now
        n = n >> 1
        x = (x**2) % m

    return a
    
for i in range(int(input())):
    n = int(input()) - 1
    print(ans(2, n))