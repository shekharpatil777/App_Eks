# Detect duplicates
nums = [1, 2, 3, 1, 4]
print(len(nums) != len(set(nums)))  # True

# Two sum problem
nums = [2, 7, 11, 15]
target = 9
seen = {}
for i, num in enumerate(nums):
    if target - num in seen:
        print((seen[target-num], i))  # (0, 1)
    seen[num] = i

