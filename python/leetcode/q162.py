class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)

        # Ensure s is the shorter string to simplify logic
        if ns > nt:
            return self.isOneEditDistance(t, s)

        # If length difference is more than 1, not one edit distance
        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                # If lengths are equal, it must be a replacement
                if ns == nt:
                    return s[i+1:] == t[i+1:]

                # If lengths are different, it must be an insertion into s (or deletion from t)
                else:
                    return s[i:] == t[i+1:]

        # If no mismatch found, check if t has exactly one extra character at the end
        return ns + 1 == nt