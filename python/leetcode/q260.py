from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        # Rightmost set bit
        diff = xor & -xor

        a = 0
        b = 0
