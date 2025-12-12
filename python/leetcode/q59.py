class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ans = [[0] * n for _ in range(n)]
        
        # Initialize boundaries and starting value
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        
        while num <= n * n:
            # 1. Traverse Right (Top Row)
            for i in range(left, right + 1):
                ans[top][i] = num
                num += 1
            top += 1
            
            # 2. Traverse Down (Right Column)
            for i in range(top, bottom + 1):
                ans[i][right] = num
                num += 1
            right -= 1
            
            # Check for boundary cross (only necessary for the last layer)
            if top <= bottom:
                # 3. Traverse Left (Bottom Row)
                for i in range(right, left - 1, -1):
                    ans[bottom][i] = num
                    num += 1
                bottom -= 1
            
   
