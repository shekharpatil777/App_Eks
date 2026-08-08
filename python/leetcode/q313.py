from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)

        ugly = [1] * n
        pointers = [0] * k
        values = primes[:]
