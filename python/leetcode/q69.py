class Solution:
    def mySqrt(self, x: int) -> int:
        # Base cases: square root of 0 is 0, and 1 is 1
        if x < 2:
            return x
        
        left, right = 1, x // 2
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
