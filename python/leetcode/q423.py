from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        digits = [0] * 10
        
        # Unique identifiers
        digits[0] = count['z']
        digits[2] = count['w']
        digits[4] = count['u']
        digits[6] = count['x']
        digits[8] = count['g']
        
        # Second-order deductions
        digits[3] = count['h'] - digits[8]
        digits[5] = count['f'] - digits[4]
        digits[7] = count['s'] - digits[6]
        
        # Third-order deductions
        digits[1] = count['o'] - digits[0] - digits[2] - digits[4]
        digits[9] = count['i'] - digits[5] - digits[6] - digits[8]
        
        # Build the sorted result string
        return "".join(str(d) * digits[d] for d in range(10))