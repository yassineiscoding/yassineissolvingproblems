class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
        return list(anagrams.values())