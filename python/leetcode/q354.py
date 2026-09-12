import bisect
from typing import List


class Solution:

  def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    if not envelopes:
      return 0

    # Sort: width ascending, height descending on tie
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    # Longest Increasing Subsequence on heights
    lis = []

    for _, h in envelopes:
      idx = bisect.bisect_left(lis, h)
      if idx < len(lis):
        lis[idx] = h
      else:
        lis.append(h)

    return len(lis)