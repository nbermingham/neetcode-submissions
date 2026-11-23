class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        abbda

        abb
        """
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # check if left removal gives pal
                left_cand = s[:left] + s[left+1:]
                right_cand = s[:right] + s[right+1:]
                if left_cand == left_cand[::-1] or right_cand == right_cand[::-1]:
                    return True
                else:
                    return False
                
                
        
        return True
        