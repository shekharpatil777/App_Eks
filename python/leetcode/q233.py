class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1
        
        while factor <= n:
            # Split n into high, curr, and low parts
            high = n // (factor * 10)
            curr = (n // factor) % 10
            low = n % factor
            
            # Apply the logic based on the current digit
            if curr == 0:
                count += high * factor
            elif curr == 1:
                count += high * factor + low + 1
            else:
                count += (high + 1) * factor
                
            # Move to the next digit place (tens -> hundreds -> thousands)
            factor *= 10
            
        return count
