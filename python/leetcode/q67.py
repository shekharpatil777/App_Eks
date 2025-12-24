class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            # Get the digit value or 0 if we've run out of digits
            val_a = int(a[i]) if i >= 0 else 0
            val_b = int(b[j]) if j >= 0 else 0
            
            # Calculate sum and carry
            total = val_a + val_b + carry
            char = total % 2      # The digit to keep (0 or 1)
            carry = total // 2    # The value to carry over
            
            res.append(str(char))
            i -= 1
            j -= 1
        
