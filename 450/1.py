'''
Given a positive integer N, print count of set bits in it. 
'''

def count_set_bits(n):
    ctr = 0
    while(n):
        n = n&(n-1) # brian kerninghan's algorithm
        ctr += 1
    return ctr

n = int(input())
print(count_set_bits(n))