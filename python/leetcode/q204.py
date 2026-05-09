class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        # Initialize a list of booleans
        primes = [True] * n
        primes[0] = primes[1] = False
)
        
        # Only need to check up to the square root of n
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                # Slicing is much faster in Python for marking multiples
                # Start at i*i, go to n, step by i
                primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
        
        return sum(primes