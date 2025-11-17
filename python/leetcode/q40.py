class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # If number exceeds remaining target, stop
                if candidates[i] > remaining:
                    break

                backtrack(i + 1, path + [candidates[i]], remaining - candidates[i])

        backtrack(0, [], target)
        return res
