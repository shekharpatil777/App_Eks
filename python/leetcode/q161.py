class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)

        # Ensure s is the shorter string to simplify logic
        if ns > nt:
            return self.isOneEditDistance(t, s)

        # If length difference is more than 1, it's impossible
        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    # Case: Replace - remaining strings must be equal
                    return s[i + 1:] == t[i + 1:]
                else:
                    # Case: Insert into s (or delete from t)
                    # s[i:] must match t[i+1:] because we "skipped" t[i]
                    return s[i:] == t[i + 1:]
