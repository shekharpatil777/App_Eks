class Solution:
    def grayCode(self, n: int) -> list[int]:
        # There are 2^n numbers in the sequence
        result = []
        for i in range(1 << n):
            # Apply the formula: i XOR (i / 2)
            result.append(i ^ (i >> 1))
        return result