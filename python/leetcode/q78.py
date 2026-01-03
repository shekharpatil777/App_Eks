class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def dfs(i):
            # Base case: if we have considered all elements
            if i >= len(nums):
                res.append(subset[:]) # Append a copy of the current subset
                return
            
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
