class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1
        
        while factor <= n:
            # Split n into high, curr, and low parts
            high = n // (factor * 10)
            curr = (n // factor) % 10
            low = n % factor
            
