class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        # A valid time cannot exceed 8 bits (max is 11:59 -> 3 bits + 5 bits = 8)
        if turnedOn > 8:
            return []
 