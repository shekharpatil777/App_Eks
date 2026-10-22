class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        # Compute F(0)
        current_val = sum(i * num for i, num in enumerate(nums))
        max_val = current_val
        
        # Compute F(1) through F(n-1) using the recurrence relation
        for k in range(1, n):
            # Element that shifts from weight (n-1) to weight 0
            dropped_element = nums[n - k]
            current_val += total_sum - n * dropped_element
            if current_val > max_val:
                max_val = current_val
                
        return max_val