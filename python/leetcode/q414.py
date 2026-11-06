class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = None

        for n in nums:
            # Skip duplicates to ensure distinct maximums
            if n in (first, second, third):
                continue
