class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Use two maps to ensure a unique bi-directional mapping
        mapST, mapTS = {}, {}

        for charS, charT in zip(s, t):
            # If charS was already mapped to something else, return False
            if charS in mapST and mapST[charS] != charT:
                return False
            
            # If charT was already mapped from a different charS, return False
            if charT in mapTS and mapTS[charT] != charS:
                return False

            # Establish the mapping
            mapST[charS] = charT
            mapTS[charT] = charS

        return True