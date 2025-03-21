class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n == 1 : return s
        left, right = 0, n - 1
        while left <= right:
            if s[left] != s[right]:
                s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        


        