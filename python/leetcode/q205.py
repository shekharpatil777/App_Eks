class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be isomorphic
        if len(s) != len(t):
            return False
        
        # Dictionaries to store the mappings
        mapST, mapTS = {}, {}

        for charS, charT in zip(s, t):
            # Check if charS is already mapped to something else
            if charS in mapST and mapST[charS] != charT:
                return False
            
            # Check if charT is already mapped to something else
            if charT in mapTS and mapTS[charT] != charS:
                return False
            
            # Establish the mapping
            mapST[charS] = charT
            mapTS[charT] = charS
            
        return True