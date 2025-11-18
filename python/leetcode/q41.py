class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return

            prev = -1
            for i in range(start, len(candidates)):
                # Skip duplicates in same level
                if candidates[i] == prev:
                    continue


