class Solution(object):
    def twoSum(self, nums, target):
        seen_numbers = {}

        # Iterate through the list with both the index and the value.
        for index, num in enumerate(nums):
            # Calculate the required complement to reach the target.
            complement = target - num

            # Check if the complement already exists in our dictionary.
            # This check is O(1) on average.
            if complement in seen_numbers:
                # If the complement is found, we've found our pair.
                # Return the current index and the index of the complement.
                return [seen_numbers[complement], index]

            # If the complement is not found, add the current number and its index
            # to the dictionary for future checks.
            seen_numbers[num] = index
