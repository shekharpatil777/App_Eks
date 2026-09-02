class Solution:
    def integerBreak(self, n: int) -> int:
        # Base constraints: k >= 2
        if n == 2:
            return 1
        if n == 3:
            return 2
