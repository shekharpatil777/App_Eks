class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # Initialize the row with 1, then expand it
        row = [1] * (rowIndex + 1)
        
