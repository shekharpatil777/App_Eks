def longestConsecutive(nums):
    # Convert to set for O(1) lookups
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Check if 'num' is the start of a sequence
        # If num - 1 is in the set, then 'num' is NOT the start
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

