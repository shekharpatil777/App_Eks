class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

       # If needle is empty, return 0 as per problem statement
        if not needle:
            return 0
        # Use built-in find() for simplicity and efficiency
        return haystack.find(needle)
