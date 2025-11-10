from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the index of the first element >= target
        first_occurrence_index = bisect_left(nums, target)
        
        # Check if the target was actually found
        if first_occurrence_index == len(nums) or nums[first_occurrence_index] != target:
            return [-1, -1]
        
        # Find the index of the first element > target, then subtract 1
        # bisect_right returns the insertion point AFTER all target occurrences
