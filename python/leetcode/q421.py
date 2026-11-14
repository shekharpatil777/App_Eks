class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        max_xor = 0
        mask = 0

        # Check bits from MSB (30) down to LSB (0)
        # Numbers are <= 2^31 - 1, so 31 bits (0 to 30) are sufficient.
        for i in range(30, -1, -1):
            # Mask to keep prefixes up to bit i
            mask |= (1 << i)

            # Store the prefixes of all numbers up to bit i
            prefixes = {num & mask for num in nums}

            # Greedily assume the i-th bit in max_xor can be 1
            candidate = max_xor | (1 << i)

            # Property: If a ^ b = candidate, then a ^ candidate = b
            for prefix in prefixes:
                if (prefix ^ candidate) in prefixes:
                    max_xor = candidate
                    break

        return max_xor