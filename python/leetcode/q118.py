class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Initialize the result list with the first row
        triangle = []
        
        for i in range(numRows):
            # Create a row filled with 1s (size is i + 1)
            row = [1] * (i + 1)
            

            # Fill the middle elements (from index 1 to i-1)
            # This loop won't run for the first two rows
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
            triangle.append(row)
            
        return triangle