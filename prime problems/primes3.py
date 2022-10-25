import math
import sys

# Assuming I am hired by facebook, this is the code I would write for the 
# version 1 for the first code review 
# in case if naming conventions are not Python standard, I apologize:
# this is my second day on Python, mostly C# before

def primesEr(N):
    sieve = set(range(2, N))
    for i in range(2, int(math.sqrt(N))):
        if i in sieve:
            sieve -= set(range(2*i, N, i))

    return sieve

def primesum(even):
    if (even <= 3) or (even % 2 != 0):
        raise Exception("by contract, number has to be even and greater than two")
    primes = sorted(list(primesEr(even*2))) # taking care of lexicographic ordering requirement

    i = -1 
    for a in primes:
        i += 1
        for b in primes[i:]:
            if (a + b == even):
                return a, b # since primes list is sorted, a <= b requirement is fulfilled
    raise Exception("ERROR: Goldbach's conjecture is WRONG. Escalate to CEO immediately!")

# MAIN
print(primesum(1000000))
