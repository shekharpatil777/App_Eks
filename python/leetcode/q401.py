class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        # A valid time cannot exceed 8 bits (max is 11:59 -> 3 bits + 5 bits = 8)
        if turnedOn > 8:
            return []
       
        valid_times = []
        for h in range(12):
            for m in range(60):
                # Count total set bits for hour and minute
                if (h.bit_count() + m.bit_count()) == turnedOn:
                    valid_times.append(f"{h}:{m:02d}")
                    
        return valid_times 