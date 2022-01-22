t = int(input())

# f( f( f(t) + t) + f( f(t) ) )

maps = {}


def f(x): return x*x + 2*x + 3


print(f(f(f(t)+t)+f(f(t))))
