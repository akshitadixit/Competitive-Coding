n = int(input())
if n in range(-(2**31), 2**31):
    print("Yes")
else:
    print("No")
