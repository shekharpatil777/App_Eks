class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Initialize the result list with the first row
        triangle = []
        
        for i in range(numRows):
            # Create a row filled with 1s (size is i + 1)
            row = [1] * (i + 1)
            
