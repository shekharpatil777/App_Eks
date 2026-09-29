class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0] * (length + 1)

        for start, end, inc in updates:
            diff[start] += inc
            diff[end + 1] -= inc

        ans = [0] * length
        curr = 0

        for i in range(length):
            curr += diff[i]
            ans[i] = curr

        return ans