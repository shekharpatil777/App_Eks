import math

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        
        hi, lo, n = max(nums), min(nums), len(nums)
        if hi == lo:
            return 0
        
        # Determine bucket size and count
        bucket_size = max(1, (hi - lo) // (n - 1))
        bucket_count = (hi - lo) // bucket_size + 1
        
        # Buckets to store the min and max values seen in that range
        buckets_min = [float('inf')] * bucket_count
        buckets_max = [float('-inf')] * bucket_count
        
        # Fill buckets
        for x in nums:
            idx = (x - lo) // bucket_size
            buckets_min[idx] = min(buckets_min[idx], x)
            buckets_max[idx] = max(buckets_max[idx], x)
            
        # Calculate the max gap
        max_gap = 0
        prev_max = lo
        
