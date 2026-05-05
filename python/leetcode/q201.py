class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Step 1: Find the common prefix by shifting right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
