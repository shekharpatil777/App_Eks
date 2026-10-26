class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_len = 1
        count = 9
        start = 1

        # Step 1: Determine the number of digits in the target number
        while n > digit_len * count:
            n -= digit_len * count
            digit_len += 1
            count *= 10
            start *= 10

        # Step 2: Identify the exact number
        # (n - 1) accounts for 0-indexed offset
        target_number = start + (n - 1) // digit_len

        # Step 3: Extract the specific digit
        digit_index = (n - 1) % digit_len
        return int(str(target_number)[digit_index])