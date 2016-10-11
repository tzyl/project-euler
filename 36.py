from math import ceil


def is_palindrome(n):
    """Returns True if the number n is a palindrome."""
    s = str(n)
    for i in range(int(ceil(len(s) / 2))):
        if s[i] != s[-(1 + i)]:
            return False
    return True


def base_n(x, n):
    """Returns the integer x in base n representation."""
    if x == 0:
        return x

    digits = []
    while x:
        digits.append(x % n)
        x /= n
    return "".join([str(d) for d in digits[::-1]])


double_base_palindromes = [x for x in xrange(1000000) if is_palindrome(x) and is_palindrome(base_n(x, 2))]
print sum(double_base_palindromes)
