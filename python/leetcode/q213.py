class Solution:
    def rob(self, nums: list[int]) -> int:
        # Edge cases: if there's only 1 house, just rob it. 
        # If nums is empty, return 0.
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Helper function from House Robber I (linear layout)
        def rob_linear(houses: list[int]) -> int:
            rob1, rob2 = 0, 0
            
            # Dynamic programming: track max money up to current house
            for n in houses:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        # The max of skipping the last house OR skipping the first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))