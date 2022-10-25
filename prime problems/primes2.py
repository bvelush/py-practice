import math
import sys

# Assuming I am hired by facebook, this is the code I would write for the 
# version 1 of the production-quality code. 
# in case if naming conventions are not Python standard, I apologize:
# this is my second day on Python, mostly C# before

def primesEr(N):
    sieve = set(range(2, N))
    for i in range(2, int(math.sqrt(N))):
        if i in sieve:
            sieve -= set(range(2*i, N, i))
    
    # ATTENTION: returning set is not sorted, because sorting is not 
    # applicable to sets. Why not sorted? Because separation of concerns
    # Why set? Because I wanted to make sure no one even ASSUMES it is sorted
    # this way it's more maintainable
    return sieve

def primesum(evenN):
    if (evenN <= 3) or (evenN % 2 != 0):
        raise Exception("by contract, number has to be even and greater than two")
    primes = list(primesEr(evenN*2)) # .sort will ensure that the first solution 
                                            # is the best "lexicographically smaller solution"
    bestSolution = (sys.maxsize, sys.maxsize)
    i = -1 # it has to be 0 and i++ should be after the inner loop. 
    # But this looks to me more maintainable because there's no "loose" i+=1 at the end
    # Could anyone review and give me feedback?
    for a in primes:
        i += 1
        for b in primes[i:]:
            if (a + b == evenN):
                # since primes list not sorted, we have to take care of two things:
                candidate = min(a, b), max(a, b)    # ... tuple order (see the spec)

                # ... and 
                print(candidate)
                if bestSolution > candidate:
                    bestSolution = candidate
                    print(bestSolution)
                    print("\n")

    return bestSolution # We KNOW it exists well in limits of 
                        # sys.maxsize and available performance


# MAIN
print(primesum(84))