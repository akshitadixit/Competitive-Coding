s = input()


def palindrome(s):
    if s == s[::-1]:
        return True
    return False


mid = s.strip('a').count('a')
end = s.lstrip('a').count('a') - mid
fwd = s.rstrip('a').count('a') - mid

if fwd <= end and palindrome(s.strip('a')):
    print("Yes")
else:
    print('No')
