class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # 1. Find the first decreasing element from the right (pivot)
        # Search for index i such that nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # 2. If such an element exists, find the smallest element to its right
        # that is greater than nums[i], and swap them.
        if i >= 0:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            


# Example usage (as the function modifies in-place, it returns None):
# nums = [1, 2, 3]
# Solution().nextPermutation(nums)
# print(nums) # Output: [1, 3, 2]

# nums = [3, 2, 1]
# Solution().nextPermutation(nums)
# print(nums) # Output: [1, 2, 3]