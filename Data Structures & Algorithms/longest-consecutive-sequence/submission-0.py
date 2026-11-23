class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        create a hashmap with the key as the number we're looking for, and the value as the
        longest consecutive sequence leading up to that number.

        """
        d = dict()
        max_sequence = 0
        for num in nums:
            if num in d:
                continue
            
            if num - 1 in d:
                before = d[num-1][0] + 1
            else:
                before = 0
            
            if num + 1 in d:
                after = d[num+1][1] + 1
            else:
                after = 0
            
            current_len = before + after + 1
            max_sequence = max(max_sequence, current_len)

            d[num] = [before, after]
            if num - before in d:
                d[num - before][1] = current_len - 1
            if num + after in d:
                d[num + after][0] = current_len - 1
        
        return max_sequence
