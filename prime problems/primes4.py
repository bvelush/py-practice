#import math
import sys

class Solution:

    def isPrime(self, A):
        if A < 2:
            return False
        if A == 2:
            return True
        for i in range(2, int((A**0.5)+1)):
            if A % i == 0:
                return False
        return True

    # Eratosphenes sieve produces sorted primes
    # @param N : integer
    # @return sorted list of primes less than N
    def EratosphenPrime(self, N):
        sieve = list(range(0, N))
        sieve[1]= 0 # 1 is not a prime
        for i in range(2, int(N**0.5)):
            if sieve[i] != 0:
                for j in range(2*i, N, i):
                    sieve[j] = 0
        result = list()
        for i in sieve:
            if i != 0:
                result.append(i) 
        return result 
    
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        if (A <= 3) or (A % 2 != 0):
            raise Exception("by contract, number has to be even and greater than two")
        
        #primes = self.EratosphenPrime(A) # sorting to take care of lexicographic ordering requirement

        #i = -1 
        for a in range(2, A):
            if (self.isPrime(a) and self.isPrime(A - a)):
                return a, A-a


s = Solution()
#aa = s.EratosphenPrime(84)

print(s.primesum(4))
print(s.primesum(84))
print(s.primesum(86))
print(s.primesum(8400))
print(s.primesum(84000))
print(s.primesum(1000000))
print(s.primesum(10000000))


# my solution. 
# import sys

# class Solution:

#     def isPrime(self, A):
#         if A < 2:
#             return False
#         if A == 2:
#             return True
#         for i in range(2, int((A**0.5)+1)):
#             if A % i == 0:
#                 return False
#         return True
    
#     # @param A : integer
#     # @return a list of integers
#     def primesum(self, A):
#         if (A <= 3) or (A % 2 != 0):
#             raise Exception("by contract, number has to be even and greater than two")
        
#         for a in range(2, A):
#             if (self.isPrime(a) and self.isPrime(A - a)):
#                 return a, A-a
#         raise Exception("ERROR: Goldbach's conjecture is WRONG. Escalate to CEO immediately!")

