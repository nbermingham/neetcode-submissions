class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        """
        anagram_group = dict()

        for s in strs:
            d = [0] * 26

            for char in s:
                d[ord(char) - ord("a")] += 1
            
            anagram_group.setdefault(tuple(d), []).append(s)
        
        return [v for v in anagram_group.values()]



        