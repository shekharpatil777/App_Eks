class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the strings into lists of components
        v1_split = version1.split('.')
        v2_split = version2.split('.')
        
        n1, n2 = len(v1_split), len(v2_split)
        
        # Iterate through the maximum possible length
        for i in range(max(n1, n2)):
            # Get the integer value or 0 if index is out of bounds
            # This handles cases like "1.1" vs "1.1.0"
            num1 = int(v1_split[i]) if i < n1 else 0
            num2 = int(v2_split[i]) if i < n2 else 0
            
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        
        # If all segments are equal
        return 0