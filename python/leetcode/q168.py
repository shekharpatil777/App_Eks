class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            # Subtract 1 to adjust for 1-indexing
            columnNumber -= 1
            
            # Get the remainder (0-25)
            remainder = columnNumber % 26
