class Solution:
    def minAbbreviation(self, target: str, dictionary: list[str]) -> str:
        n = len(target)
        # Filter dictionary to only words of the exact same length as target
        diff_masks = []
        for word in dictionary:
            if len(word) != n:
                continue
            # Build a bitmask of mismatched characters
            mask = 0
            for i in range(n):
                if target[i] != word[i]:
                    mask |= (1 << (n - 1 - i))
            diff_masks.append(mask)

        # If no words in dictionary have the same length, abbreviate the whole string
        if not diff_masks:
            return str(n)

        # Precompute the abbreviation length for any bitmask of preserved characters
        def abbr_length(mask: int) -> int:
            length = 0
            consecutive_zeros = 0
            for i in range(n):
                if (mask >> (n - 1 - i)) & 1:
                    if consecutive_zeros > 0:
                        length += 1
                        consecutive_zeros = 0
                    length += 1
                else:
                    consecutive_zeros += 1
            if consecutive_zeros > 0:
                length += 1
            return length

        # Convert a bitmask into the final abbreviation string
        def to_abbr(mask: int) -> str:
            res = []
            count = 0
            for i in range(n):
                if (mask >> (n - 1 - i)) & 1:
