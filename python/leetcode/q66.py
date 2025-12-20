class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Iterate from the end of the list to the beginning
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # No carry needed, just increment and return
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 and we carry over
            digits[i] = 0
