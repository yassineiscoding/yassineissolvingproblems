import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        s = "".join(c for c in s.lower() if c not in string.punctuation and c != " ")
        # Two pointers
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
