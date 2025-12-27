class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # 'first' represents n-2, 'second' represents n-1
        first, second = 1, 2
        
