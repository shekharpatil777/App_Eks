class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is greater than the far right element, 
            # the min must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the min is in the left half (including mid).
            else:
                right = mid
                
        return nums[left]