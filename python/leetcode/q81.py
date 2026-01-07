class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return True
            
            # The critical check for duplicates
            # If left, mid, and right are the same, we can't tell which side is sorted
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            
            # Identify which half is sorted
            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted

