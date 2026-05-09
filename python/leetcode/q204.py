class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        # Initialize a list of booleans
        primes = [True] * n
        primes[0] = primes[1] = False
)