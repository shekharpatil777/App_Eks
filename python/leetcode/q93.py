class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        if len(s) > 12:  # Quick check: maximum length of a valid IP is 12 digits
            return res

        def backtrack(start, path):
            # Base case: if we have 4 segments and reached the end of the string
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            # Try taking 1, 2, or 3 digits for the next segment
            for length in range(1, 4):
                if start + length > len(s):
                    break
                
                segment = s[start : start + length]
                
                # Check for validity:
                # 1. No leading zeros (unless the segment is just "0")
                # 2. Value must be between 0 and 255
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue

