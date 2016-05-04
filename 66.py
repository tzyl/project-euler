def solve_quadratic_diophantine(D):
    """
    Solves the quadratic Diophantine equation x^2 - D*y^2 = 1.
    Returns the solution (x, y) which is minimal in x.
    """
    if int(D ** 0.5) ** 2 == D:
        return None

    first_convergent, peridoic_convergents = continued_fraction(D)

    # Set up convergents for recurrence relation.
    A = [first_convergent]
    B = [1]
    B.append(peridoic_convergents[0])
    A.append(A[0]*B[1] + 1)

    # Check if these base cases solve the equation.
    for (x, y) in zip(A, B):
        if x**2 - D * y**2 == 1:
            return (x, y)

    n = 2
    while True:
        b = peridoic_convergents[(n - 1) % len(peridoic_convergents)]

        x = b * A[-1] + A[-2]
        y = b * B[-1] + B[-2]

        if x**2 - D * y**2 == 1:
            return (x, y)
        else:
            A.append(x)
            B.append(y)
            n += 1


def continued_fraction(n):
    if int(D ** 0.5) ** 2 == D:
        return None

    m = 0
    d = 1
    a = int(n ** 0.5)
    seen = set()

    first_convergent = a
    peridoic_convergents = []

    m = d*a - m
    d = (n - m**2) / d
    a = int((first_convergent + m) / d)

    while (m, d, a) not in seen:
        peridoic_convergents.append(a)
        seen.add((m, d, a))
        m = d*a - m
        d = (n - m**2) / d
        a = int((first_convergent + m) / d)

    return first_convergent, peridoic_convergents

solns = []
for D in xrange(1001):
    soln = solve_quadratic_diophantine(D)
    if soln is not None:
        solns.append((D, soln))

print max(solns, key=lambda (D, soln): soln[0])
