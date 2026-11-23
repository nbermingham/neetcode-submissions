class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        start with a left and right pointer at index 0. We keep track of a counter hashmap with the count of every character in the substring. We move the right pointer to the right, adding 1 to that characters count in the hashmap. 
        
        If the characters count isn't >1, we compare r - l + 1 to the max_length, replace if bigger

        If it IS greater than 1, we move the left pointer to the right, subtracting from the hashmap until we find that character and it's 1 again.

        return the max_length at the end.
        """

        max_length = 0

        l, r = 0, 0

        chars = set()

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            max_length = max(max_length, len(chars))
        
        return max_length
