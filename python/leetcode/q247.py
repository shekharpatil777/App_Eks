class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        def build(length, total):
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]

            middle = build(length - 2, total)
            result = []

            for num in middle:
                if length != total:  # Avoid leading zero
                    result.append("0" + num + "0")
