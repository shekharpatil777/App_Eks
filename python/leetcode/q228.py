class Solution:

    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        ranges = []
        start = nums[0]

        for i in range(len(nums)):
            # Check if we are at the last element or if the next element is not consecutive
            if i == len(nums) - 1 or nums[i + 1] != nums[i] + 1:
                # If start is equal to the current element, it's a single number
                if start == nums[i]:
                    ranges.append(str(start))
                else:
                    # Otherwise, it's a range
                    ranges.append(f"{start}->{nums[i]}")
