class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []
        n = len(nums)

        def backtrack(current_permutation):
            # Base Case: If the current permutation is complete, add it to results
            if len(current_permutation) == n:
                # We append a copy to avoid issues with Python's list references
                results.append(list(current_permutation))
                return

            # Recursive Step: Try adding every unused number
            for num in nums:
                if num not in current_permutation:
                    # 1. Choose: Add the number to the current permutation
                    current_permutation.append(num)
                    
                    # 2. Explore: Recurse to find the rest of the permutation
                    backtrack(current_permutation)
                    
                    # 3. Unchoose (Backtrack): Remove the number to explore other branches
                    current_permutation.pop()

