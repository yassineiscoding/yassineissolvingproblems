class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_word = ""
        len1 = len(word1)
        len2 = len(word2)
        for i in range(max(len1, len2)):
            if i < len1:
                final_word += word1[i]
            if i < len2:
                final_word += word2[i]
        
        return final_word


       





