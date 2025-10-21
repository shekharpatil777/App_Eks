class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Sort the array to enable the two-pointer technique
        nums.sort()
        n = len(nums)
        
        # Initialize the closest_sum with the sum of the first three elements
        # A very large initial difference (like float('inf')) can also be used, 
        # but initializing with an actual sum is often cleaner.
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # Iterate through the array, fixing the first element `nums[i]`
        for i in range(n - 2):
            # Initialize two pointers: `left` to the element after `i`
            # and `right` to the last element
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Check if the current sum is closer to the target than the closest_sum found so far
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # If the current sum is exactly the target, we can return immediately 
                # because the problem guarantees exactly one solution, and this is the closest possible.
                if current_sum == target:
                    return current_sum
                
                # Adjust pointers based on the comparison with the target
                elif current_sum < target:
                    # Sum is too small, need a larger sum, so move the left pointer to the right
                    left += 1
                else: # current_sum > target
                    # Sum is too large, need a smaller sum, so move the right pointer to the left
                    right -= 1
                    
        return closest_sum