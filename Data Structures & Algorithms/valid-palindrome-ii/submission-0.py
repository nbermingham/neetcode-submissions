class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        abbda

        abb
        """
        
        
        for i in range(len(s)):
            cand = s[:i] + s[i+1:]
            if cand == cand[::-1]:
                return True
        
        return False
        