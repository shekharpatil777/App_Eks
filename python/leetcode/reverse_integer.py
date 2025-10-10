class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit integer boundaries
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Handle the sign separately
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        while x != 0:
            # Pop the last digit
            digit = x % 10
            x //= 10
            
            # Check for potential overflow BEFORE the operation
            # For positive numbers
            if sign == 1:
                if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 7):
                    return 0
            # For negative numbers
            else:
                # The check is against abs(INT_MIN), which is 2**31
                if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 8):
                    return 0

            # Push the digit
            reversed_num = reversed_num * 10 + digit
            
        return sign * reversed_num