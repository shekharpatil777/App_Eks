class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def is_valid(first: int, second: int, index: int) -> bool:
            while index < n:
                third = first + second
                third_str = str(third)

                if not num.startswith(third_str, index):
                    return False

                index += len(third_str)
                first, second = second, third

            return True

        # Choose the first number
        for i in range(1, n):
            # First number cannot have a leading zero
            if num[0] == "0" and i > 1:
                break

            # Choose the second number
            for j in range(i + 1, n):
                # Second number cannot have a leading zero
                if num[i] == "0" and j - i > 1:
                    break

                first = int(num[:i])
                second = int(num[i:j])

                if is_valid(first, second, j):
                    return True

        return False