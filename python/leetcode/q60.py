class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # Initialize an n x n matrix filled with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Initialize boundary pointers
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        # Start filling number
        num = 1
        
        while num <= n * n:
            
            # 1. Traverse Right (Top Row)
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1
            
            # 2. Traverse Down (Right Column)
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # 3. Traverse Left (Bottom Row) - Only if boundaries haven't crossed
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1
            
            # 4. Traverse Up (Left Column) - Only if boundaries haven't crossed

                
        return matrix

# Example usage (for n=3, it should return [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
# print(Solution().generateMatrix(3))
