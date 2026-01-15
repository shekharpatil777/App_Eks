class Solution:
    def grayCode(self, n: int) -> list[int]:
        # Start with the base case for n = 0
        result = [0]
        
        for i in range(n):
            # The value to add to the mirrored part (2^i)
            mask = 1 << i
            
