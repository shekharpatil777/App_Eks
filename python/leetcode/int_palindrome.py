class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        original = x
        reversed_num = 0



        return original == reversed_num
