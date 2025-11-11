from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize the left pointer to the start of the array
        left = 0
        # Initialize the right pointer to the length of the array (exclusive end)
        # Setting 'right' to len(nums) allows us to handle insertion at the very end.
        right = len(nums)
        
        # The loop continues as long as the search space is valid
        while left < right:
            # Calculate the middle index
            mid = left + (right - left) // 2
            
            # If the middle element is the target, we found it
            if nums[mid] == target:
                return mid
            
            # If the middle element is less than the target,
            # the target must be in the right half (after mid).
            # We discard the left half by setting left = mid + 1.
            elif nums[mid] < target:
                left = mid + 1
            
            # If the middle element is greater than the target,
            # the target must be at or before the mid position.
            # We set right = mid, keeping 'mid' as a potential answer.
            else: # nums[mid] > target
                right = mid
        
 