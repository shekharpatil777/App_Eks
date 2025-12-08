from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True # Should not happen based on problem constraints, but good practice
        
        # Initialize the 'goal' to the last index
        goal = len(nums) - 1
        
        # Iterate backward from the second-to-last element down to the first (index 0)
        # range(start, stop, step) -> stop is exclusive
        for i in range(len(nums) - 2, -1, -1):
            
            # Check if we can reach the current 'goal' from the current position 'i'
            if i + nums[i] >= goal:
                # If we can reach the current goal, this position 'i' becomes the new, 
                # closer goal we need to reach.
                goal = i

                
        # If the goal has been successfully moved back to index 0, we can reach the end.
        return goal == 0