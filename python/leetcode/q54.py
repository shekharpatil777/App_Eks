from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        rows, cols = len(matrix), len(matrix[0])
        
        # Initialize the boundary pointers
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        
        while len(result) < rows * cols:
            
            # 1. Traverse Right (Top row)
            # Stop if the top boundary has crossed the bottom one
            if top <= bottom:
                for j in range(left, right + 1):
                    result.append(matrix[top][j])
                top += 1 # Shrink the top boundary inward
            
            # 2. Traverse Down (Right column)
            # Stop if the right boundary has crossed the left one
            if left <= right:
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1 # Shrink the right boundary inward
            
            # 3. Traverse Left (Bottom row)
            # Need to re-check the boundary condition because it might have changed 
            # after the previous two steps (especially for non-square matrices)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1 # Shrink the bottom boundary inward
            
            # 4. Traverse Up (Left column)
            # Need to re-check the boundary condition
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1 # Shrink the left boundary inward
                
        return result