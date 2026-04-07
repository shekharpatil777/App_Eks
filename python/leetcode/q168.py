class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            # Subtract 1 to adjust for 1-indexing
            columnNumber -= 1
            
            # Get the remainder (0-25)
            remainder = columnNumber % 26
            
            # Convert to character (ord('A') is 65)
            char = chr(65 + remainder)
            result.append(char)
            
            # Move to the next "digit"
            columnNumber //= 26
            
        # The characters were added in reverse order (units first)
        return "".join(reversed(result))