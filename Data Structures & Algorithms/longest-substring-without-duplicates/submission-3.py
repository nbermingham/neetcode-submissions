class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        chars = set()
        l = 0

        for r in range(len(s)):
            if s[r] in chars:
                while s[l] != s[r]:
                    chars.discard(s[l])
                    l += 1
                l += 1
            max_length = max(r - l + 1, max_length)
            chars.add(s[r])

        
        return max_length
            
