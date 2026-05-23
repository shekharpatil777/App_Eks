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
