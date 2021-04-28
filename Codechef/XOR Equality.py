# by laws of xor algebra:
# x^(x+1)^(x+2)^(x+3) = 0
# now x = 2k for the above to hold true i.e. x%2==0

m = 1000000007
for _ in range(int(input())):
	n = int(input())
	n = 2**n - 1
	r = n//2 +1 # no. of multiples of 4
	print(r%m)