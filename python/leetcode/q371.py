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
