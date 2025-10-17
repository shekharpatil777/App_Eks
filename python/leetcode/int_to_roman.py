class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the value and symbol pairs in descending order,
        # including the subtractive forms (e.g., 900 for 'CM', 40 for 'XL').
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
            (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
            (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        result = ""
        
        for value, symbol in value_symbols:
            # Check how many times the current value can be subtracted from num
            if num == 0:
                break
            
            # Use divmod for efficiency: count is how many times, num is the remainder
            count, num = divmod(num, value)

            
        return result