class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        l = 0
        while l < len(nums):
            r = l
            while nums[r]+1 in nums:
                r += 1
            if l == r:
                res.append(f'{nums[l]}')
            else:
                res.append(f'{nums[l]}->{nums[r]}')
            l = r+1
        return res       