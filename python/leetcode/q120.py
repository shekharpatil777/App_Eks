class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # Initialize the row with 1, then expand it
        row = [1] * (rowIndex + 1)
        
        # We start from the 2nd row (index 2) because rows 0 and 1 
        # are already correctly handled by the initialization
        for i in range(2, rowIndex + 1):
            # Update middle elements backwards to avoid overwriting
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j-1]
                
        return row