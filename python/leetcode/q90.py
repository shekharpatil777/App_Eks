class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Step 1: Sort to handle duplicates
        
        def backtrack(start, path):
            # Add a copy of the current path to results
            res.append(list(path))
            
            for i in range(start, len(nums)):
                # Step 2: Skip duplicates
                # If nums[i] is same as nums[i-1], and we aren't at the 'start' index,
                # it means we've already processed this value in this position.
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop() # Backtrack
                
        backtrack(0, [])
        return res