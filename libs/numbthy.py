######################################################################################
# NUMBTHY.PY
# Basic Number Theory functions implemented in Python
# Note: Currently requires Python 2.x (uses +=, %= and other 2.x-isms)
# Note: Currently requires Python 2.3 (uses implicit long integers - could be back-ported though)
# Author: Robert Campbell, <campbell@math.umbc.edu>
# Date: 27 April, 2007
# Version 0.41
######################################################################################
"""Basic number theory functions.
   Functions implemented are:
        gcd(a,b) - Compute the greatest common divisor of a and b.
        xgcd(a,b) - Find [g,x,y] such that g=gcd(a,b) and g = ax + by.
        powmod(b,e,n) - Compute b^e mod n efficiently.
        isprime(n) - Test whether n is prime using a variety of pseudoprime tests.
        isprimeF(n,b) - Test whether n is prime or a Fermat pseudoprime to base b.
        isprimeE(n,b) - Test whether n is prime or an Euler pseudoprime to base b.
        eulerphi(n) - Computer Euler's Phi function of n - the number of integers strictly less than n which are coprime to n.
        carmichaellambda(n) - Computer Carmichael's Lambda function of n - the smallest exponent e such that b**e = 1 for all b coprime to n.
        factor(n) - Find a factor of n using a variety of methods.
        factors(n) - Return a sorted list of the prime factors of n.
        factorPR(n) - Find a factor of n using the Pollard Rho method
        isprimitive(g,n) - Test whether g is primitive - generates the group of units mod n.
   A list of the functions implemented in numbthy is printed by the command info()."""

import math  # Use sqrt, floor

SMALL_PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}


def gcd(a, b):
    """gcd(a,b) returns the greatest common divisor of the integers a and b."""
    if a == 0:
        return b
    return abs(gcd(b % a, a))


def powmod(b, e, n):
    """powmod(b,e,n) computes the eth power of b mod n.
    (Actually, this is not needed, as pow(b,e,n) does the same thing for positive integers.
    This will be useful in future for non-integers or inverses."""
    accum, i, bpow2 = 1, 0, b
    while (e >> i) > 0:
        if (e >> i) & 1:
            accum = (accum * bpow2) % n
        bpow2 = (bpow2 * bpow2) % n
        i += 1
    return accum


def xgcd(a, b):
    """xgcd(a,b) returns a list of form [g,x,y], where g is gcd(a,b) and
    x,y satisfy the equation g = ax + by."""
    a1, a2 = 1, 0
    b1, b2 = 0, 1
    aneg, bneg = 1, 1
    swap = False
    if a < 0:
        a = -a
        aneg = -1
    if b < 0:
        b = -b
        bneg = -1
    if b > a:
        swap = True
        a, b = b, a
    while True:
        quot = -a / b
        a = a % b
        a1 = a1 + quot * a2
        b1 = b1 + quot * b2
        if a == 0:
            out1, out2 = b2 * bneg, a2 * aneg
            if swap:
                out1, out2 = out2, out1
            return out1, out2

        b, a = a, b
        a1, a2 = a2, a1
        b1, b2 = b2, b1


def isprime(n):
    """isprime(n) - Test whether n is prime using a variety of pseudoprime tests."""
    if n in SMALL_PRIMES:
        return True
    return isprimeE(n, 2) and isprimeE(n, 3) and isprimeE(n, 5)


def isprimeF(n, b):
    """isprimeF(n) - Test whether n is prime or a Fermat pseudoprime to base b."""
    return pow(b, n - 1, n) == 1


def isprimeE(n, b):
    """isprimeE(n) - Test whether n is prime or an Euler pseudoprime to base b."""
    if not isprimeF(n, b):
        return False
    r = n - 1
    while (r % 2 == 0):
        r /= 2
    c = pow(b, r, n)
    if (c == 1):
        return True
    while (1):
        if (c == 1):
            return False
        if (c == n - 1):
            return True
        c = pow(c, 2, n)


def factor(n):
    """factor(n) - Find a prime factor of n using a variety of methods."""
    if isprime(n):
        return n
    for fact in SMALL_PRIMES:
        if n % fact == 0:
            return fact
    return factorPR(n)  # Needs work - no guarantee that a prime factor will be returned


def factors(n):
    """factors(n) - Return a sorted list of the prime factors of n."""
    if (isprime(n)):
        return [n]
    fact = factor(n)
    if (fact == 1):
        return "Unable to factor {}".format(n)
    facts = factors(n / fact) + factors(fact)
    return sorted(facts)


def factorPR(n):
    """factorPR(n) - Find a factor of n using the Pollard Rho method.
    Note: This method will occasionally fail."""
    for slow in [2, 3, 4, 6]:
        fast = slow
        numsteps = 2 * math.floor(math.sqrt(math.sqrt(n)))
        for i in range(1, numsteps):
            slow = (slow * slow + 1) % n
            fast = (fast * fast + 1) % n
            fast = (fast * fast + 1) % n
            g = gcd(fast - slow, n)
            if g != 1:
                if g == n:
                    break
                return g
    return 1


def eulerphi(n):
    """eulerphi(n) - Computer Euler's Phi function of n - the number of integers
    strictly less than n which are coprime to n.  Otherwise defined as the order
    of the group of integers mod n."""
    phi = 1
    oldfact = 1
    for fact in sorted(factors(n)):
        if fact == oldfact:
            phi = phi * fact
        else:
            phi = phi * (fact - 1)
            oldfact = fact
    return phi


def carmichaellambda(n):
    """carmichaellambda(n) - Computer Carmichael's Lambda function
    of n - the smallest exponent e such that b**e = 1 for all b coprime to n.
    Otherwise defined as the exponent of the group of integers mod n."""
    thefactors = sorted(factors(n))
    thefactors += [0]  # Mark the end of the list of factors
    carlambda = 1  # The Carmichael Lambda function of n
    carlambda_comp = 1  # The Carmichael Lambda function of the component p**e
    oldfact = 1
    for fact in thefactors:
        if fact == oldfact:
            carlambda_comp = carlambda_comp * fact
        else:
            if oldfact == 2 and carlambda_comp >= 4:
                carlambda_comp /= 2  # Z_(2**e) is not cyclic for e>=3
            if carlambda == 1:
                carlambda = carlambda_comp
            else:
                carlambda_gcd = gcd(carlambda, carlambda_comp)
                carlambda = (carlambda * carlambda_comp) / carlambda_gcd
            carlambda_comp = fact - 1
            oldfact = fact
    return carlambda


def isprimitive(g, n):
    """isprimitive(g,n) - Test whether g is primitive - generates the group of units mod n."""
    if gcd(g, n) != 1:
        return False  # Not in the group of units

    order = eulerphi(n)
    if carmichaellambda(n) != order:
        return False  # Group of units isn't cyclic

    oldfact = 1
    for fact in factors(order):
        if fact != oldfact:
            if pow(g, order / fact, n) == 1:
                return False
            oldfact = fact
    return True


def info():
    """Return information about the module"""
    print locals()
