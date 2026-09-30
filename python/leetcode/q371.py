class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            # XOR computes addition without carry
            # AND followed by shift computes the carry bits
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry

        # If a exceeds the maximum positive 32-bit integer,
        # convert it to its negative two's complement value
        return a if a <= max_int else ~(a ^ mask)