class Solution:
    def integerBreak(self, n: int) -> int:
        # Base constraints: k >= 2
        if n == 2:
            return 1
        if n == 3:
            return 2

        # Count how many 3s can be formed
        quotient, remainder = divmod(n, 3)

        if remainder == 0:
            return 3**quotient
        elif remainder == 1:
            # 3 + 1 is better split as 2 * 2
            return (3 ** (quotient - 1)) * 4
        else:  # remainder == 2
            return (3**quotient) * 2