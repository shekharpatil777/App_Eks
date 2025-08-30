from itertools import accumulate
import operator

nums = [1, 2, 3, 4]
print(list(accumulate(nums)))                 # [1, 3, 6, 10] (sum)
print(list(accumulate(nums, operator.mul)))   # [1, 2, 6, 24] (product)
