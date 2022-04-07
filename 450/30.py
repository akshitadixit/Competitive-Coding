'''
Factorials of large integer N
'''

# problem is storing the "number" of digits of the answer


def factorial_large(n):
    res = list(map(int, str(n)))

    while n > 1:
        temp = []
        carry = 0
        for x in res:
            sum = x*n + carry
            if sum > 9:
                carry = int(str(sum)[:-1])
                sum = int(str(sum)[-1])
            else:
                carry = 0
            temp.append(sum)

        temp.extend(list(map(int, list(str(carry)[::-1]))))
        res = temp
        n -= 1

    return "".join(map(str, res[::-1])).lstrip('0')


print(factorial_large(100))
print(len('93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000'))
print(len(factorial_large(100)))
