class Solution:

  def canPartition(self, nums: list[int]) -> bool:
    total_sum = sum(nums)

    # If total sum is odd, it cannot be divided into two equal integer subsets
    if total_sum % 2 != 0:
      return False

    target = total_sum // 2

    # dp[j] indicates whether a subset sum of j is achievable
    dp = [False] * (target + 1)
    dp[0] = True  # A sum of 0 is always possible with an empty subset

    for num in nums:
      # If an individual number is larger than the target, return False early
      if num > target:
        return False
