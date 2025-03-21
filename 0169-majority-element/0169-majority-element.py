from math import floor
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        threshold = floor(n // 2)
        counts = defaultdict(int)
        for i in nums:
            counts[i]+=1
            if counts[i] > threshold:
                return i

        