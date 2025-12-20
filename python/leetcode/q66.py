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

            
        # If we reach here, it means all digits were 9 (like [9, 9])
        # We need to add a 1 at the start (to get [1, 0, 0])
        return [1] + digits