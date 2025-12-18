class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        # Initialize DP array with the first row's cumulative sums
        dp = [0] * cols
        dp[0] = grid[0][0]
        
        # Fill the first row
        for c in range(1, cols):
            dp[c] = dp[c-1] + grid[0][c]
            
        # Fill the rest of the grid row by row

        for r in range(1, rows):
            # Update the first element of the row (can only come from above)
            dp[0] += grid[r][0]
            for c in range(1, cols):
                # Min of (value from above, value from left) + current cell
                dp[c] = min(dp[c], dp[c-1]) + grid[r][c]
                
        return dp[-1]