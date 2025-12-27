class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # 'first' represents n-2, 'second' represents n-1
        first, second = 1, 2
        
        for i in range(3, n + 1):
            # The current step is the sum of the previous two
            current = first + second
            # Update pointers for the next iteration
            first = second
            second = current
            
        return second