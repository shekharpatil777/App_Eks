class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(max_sum: int) -> bool:
            # Helper function to check if nums can be split into <= k subarrays
            # such that no subarray sum exceeds max_sum
            current_sum = 0
            subarrays_count = 1
            
            for num in nums:
                if current_sum + num > max_sum:
                    subarrays_count += 1
                    current_sum = num
                    if subarrays_count > k:
                        return False
                else:
                    current_sum += num
            return True

        # The minimum possible largest sum is the max single element in the array.
        # The maximum possible largest sum is the sum of all elements in the array.
        low = max(nums)
        high = sum(nums)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2

            
            if canSplit(mid):
                ans = mid       # mid is a valid largest sum, try to find a smaller maximum
                high = mid - 1
            else:
                low = mid + 1   # mid is too small, increase the allowed maximum sum
                
        return ans