class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def sort_word(word):
            return ''.join(sorted(word))
        return sort_word(s) == sort_word(t)
