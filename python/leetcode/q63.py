class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        # Create a DP array initialized with 0s
        dp = [0] * cols
        
        # Starting point
        dp[0] = 1
        
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    # If there's an obstacle, no paths can pass through here
                    dp[c] = 0
                elif c > 0:
