def is_palindrome_number(x):
    """Returns True if integer x is a palindrome."""
    return str(x) == str(x)[::-1]


if __name__ == '__main__':
    largest = 0
    for a in xrange(100, 1000):
        for b in xrange(a, 1000):
            product = a * b
            if is_palindrome_number(product):
                largest = max(largest, product)
    print largest
