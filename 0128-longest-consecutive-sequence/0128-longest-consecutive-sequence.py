class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0
        for value in nums:
            if value in st and (value - 1) not in st:
                current = value
                cnt = 0
                while current in st:
                    st.remove(current)
                    current += 1
                    cnt += 1
                res = max(res, cnt)
        return res
                
        

        