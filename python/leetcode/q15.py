from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the array

        for i, a in enumerate(nums):
            # Optimization: If the current fixed number is positive, 
            # the sum of three numbers (even with the two smallest remaining) 
            # cannot be 0, so we can break early.
            if a > 0:
                break
            
            # Skip duplicates for the first fixed number 'a'
            # (only check if i > 0, as we need a previous element to compare)
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Two-Pointer setup
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1  # Sum is too large, need a smaller number from the right
                elif threeSum < 0:
                    l += 1  # Sum is too small, need a larger number from the left
                else:
                    # Found a triplet
                    res.append([a, nums[l], nums[r]])
                    
                    # Move pointers inward
                    l += 1
                    r -= 1
                    
                    # Skip duplicates for the second number (l)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    # Skip duplicates for the third number (r) - not strictly necessary 
                    # as 'r' will also be checked on the next outer loop iteration, 
                    # but it is good practice here to fully clear all duplicate pairs for 'a'

                    #     r -= 1
                        
        return res