class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            N = -n  # Use a temporary variable for the exponent
        else:
            N = n

        ans = 1.0
        
        # Binary Exponentiation (Iterative)
        while N > 0:
            # If the current bit is 1 (N is odd), include the current power of x in the result
            if N % 2 == 1:
                ans = ans * x
            
            # Square the base for the next iteration
            x = x * x
            
            # Move to the next bit (integer division by 2)
            N = N // 2
            
        return ans

# Example Usage:
# sol = Solution()
# print(sol.myPow(2.0, 10))  # Output: 1024.0
# print(sol.myPow(2.0, -2)) # Output: 0.25
