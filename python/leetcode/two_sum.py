class Solution(object):
    def twoSum(self, nums, target):
        seen_numbers = {}

        # Iterate through the list with both the index and the value.
        for index, num in enumerate(nums):
            # Calculate the required complement to reach the target.
            complement = target - num

            # Check if the complement already exists in our dictionary.
            # This check is O(1) on average.

