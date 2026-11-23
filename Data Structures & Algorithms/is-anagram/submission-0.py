class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s, counter_t = dict(), dict()
        for i in range(len(s)):
            if s[i] not in counter_s:
                counter_s[s[i]] = 1
            else:
                counter_s[s[i]] += 1
            
            if t[i] not in counter_t:
                counter_t[t[i]] = 1
            else:
                counter_t[t[i]] += 1
        
        return counter_s == counter_t
