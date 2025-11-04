class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 1. Handle the overflow edge case
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # -2^31 / -1 overflows, return INT_MAX
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # 2. Determine the sign of the result
        # The sign is negative if exactly one of them is negative (XOR logic)
        negative = (dividend < 0) ^ (divisor < 0)
        
        # 3. Convert to positive (absolute values) for easier calculation
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        quotient = 0
        
        # 4. Optimized Repeated Subtraction using Bit Shifting
        # Loop while the dividend is still greater than or equal to the divisor
        while dvd >= dvs:
            # Find the largest multiple of divisor (dvs << shift) that is less than or equal to dvd
            shift = 0
            while dvd >= (dvs << (shift + 1)):
                shift += 1
            

        # 5. Apply the correct sign
        return -quotient if negative else quotient