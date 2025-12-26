class Solution:
    def mySqrt(self, x: int) -> int:
        # Base cases: square root of 0 is 0, and 1 is 1
        if x < 2:
            return x
        
        left, right = 1, x // 2
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Avoid potential overflow by comparing mid with x // mid
            if mid <= x // mid:
                ans = mid      # mid could be the answer
                left = mid + 1 # Try to find a larger value
            else:
                right = mid - 1 # mid is too large
                
        return ans