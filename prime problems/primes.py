"""
Eratosfen's sieve, implemented on sets.abs
@param N: max prime is less than N
returns *unsorted* list of primes
"""

import math

def primes(N):
    sieve = set(range(2, N))
    for i in range(2, int(math.sqrt(N))):
        if i in sieve:
            sieve -= set(range(2*i, N, i))
    return list(sieve)

print(primes(10000000))
