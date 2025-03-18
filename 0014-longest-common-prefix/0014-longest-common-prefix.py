class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0: return ""
        
        prefix = strs[0]
        if len(strs) == 1: return prefix

        for string in strs:
            if len(string) == 0 :
                return ""
            if len(string) < len(prefix):
                prefix = string
        
        for s in strs:
            while s[:len(prefix)]!= prefix:
                prefix = prefix[:-1]
                if len(prefix) == 0 : return ""

        return prefix



