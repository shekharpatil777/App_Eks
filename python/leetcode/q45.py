class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        # If the array has only one element, 0 jumps are needed.
        if n == 1:
            return 0

        jumps = 0
        current_jump_end = 0  # The farthest index reached with 'jumps' jumps
        farthest_reachable = 0 # The overall farthest index we can reach

        # Iterate through all elements except the last one (n-1)
        for i in range(n - 1):
            # 1. Update the overall farthest reachable index
            # farthest_reachable = max(current_farthest, i + nums[i])
            farthest_reachable = max(farthest_reachable, i + nums[i])
            
            # 2. Check if we've reached the end of the current jump
            if i == current_jump_end:
                # We must make a jump. The destination of this jump 
                # will be determined by the 'farthest_reachable' we calculated 
                # in the current range.
                jumps += 1
                current_jump_end = farthest_reachable
                
