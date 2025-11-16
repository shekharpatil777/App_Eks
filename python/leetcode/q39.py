class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, curr_list, curr_sum):
            # Base case: sum reached target
            if curr_sum == target:
                res.append(curr_list[:])
                return

            # If sum exceeds target → stop exploring
            if curr_sum > target:
                return

            # Explore candidates from 'start' index to avoid duplicates
            for i in range(start, len(candidates)):
                

