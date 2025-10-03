def lengthOfLongestSubstring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    """
    # Dictionary to store the most recent index of each character
    char_map = {}
    
    # Left pointer of the window
    left = 0
    
    # Variable to store the maximum length found
    max_length = 0
    
    # Iterate through the string with the right pointer
    for right, char in enumerate(s):
        # Check if the character is already in the map AND its last occurrence
        # is within the current window (i.e., its index is >= left)
        if char in char_map and char_map[char] >= left:
            # If so, move the left pointer to the position right after
            # the last occurrence of this character to exclude the repeat.
            left = char_map[char] + 1
            
        # Update the character's last seen index to the current position
        char_map[char] = right
        
        # Calculate the length of the current window and update max_length
        current_length = right - left + 1
        max_length = max(max_length, current_length)
        
    return max_length


# Example Usage:
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3