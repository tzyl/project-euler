def is_lychrel(n):
    """
    Returns True if n is a Lychrel number assuming it is if it does not produce
    a palindrome in less than fifty iterations.
    """
    for i in xrange(50):
        n += int(str(n)[::-1])
        if is_palindrome(str(n)):
            return False
    return True


def is_palindrome(s):
    """Returns true if the string s is a palindrome."""
    return s == s[::-1]


lychrel_count = 0
for n in xrange(10000):
    if is_lychrel(n):
        lychrel_count += 1
print lychrel_count
