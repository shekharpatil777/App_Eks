class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = None

        for n in nums:
            # Skip duplicates to ensure distinct maximums
            if n in (first, second, third):
                continue

            if first is None or n > first:
                first, second, third = n, first, second
            elif second is None or n > second:
                second, third = n, second
            elif third is None or n > third:
                third = n

        # If third maximum does not exist, return the maximum (first)
        return third if third is not None else first