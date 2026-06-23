class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower_bound = float("-inf")

        for num in preorder:
            if num < lower_bound:
                return False
