class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        # Compute F(0)
        current_val = sum(i * num for i, num in enumerate(nums))
        max_val = current_val
