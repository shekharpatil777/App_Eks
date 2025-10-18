class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Map Roman symbols to their values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # 2. Initialize variables
        total = 0
        # Initialize the value of the 'previous' numeral (since we start from the right)
        prev_value = 0 
        
        # 3. Iterate from right to left (end of the string to the beginning)
        for char in reversed(s):
            current_value = roman_map[char]
            
            # 4. Check for the subtractive case
            # If the current symbol's value is less than the previous one, subtract it.
            # E.g., for 'IV', when we are at 'I' (1), prev_value is 5.
            if current_value < prev_value:
                total -= current_value
            # Otherwise, add the value
            # E.g., for 'VI', when we are at 'I' (1), prev_value is 0, so we add 1. 
            # When we are at 'V' (5), prev_value is 1, so we add 5.
            else:
                total += current_value
                

            
        return total