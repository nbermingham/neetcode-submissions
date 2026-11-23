class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        we want to return the k most frequent elements in the nums array.

        - unique cases (only one list of k elements)
        - return answer in any order

        Approach: counter
        1. walk through the array and update a counter with keys = numbers and values
        = the number of times we've seen that number
        2. sort the resulting dictionary by value descending
        3. return the top k keys of that dictionary
        """

        c = dict()

        for num in nums:
            c[num] = c.get(num, 0) + 1
        
        return [key for key, value in sorted(c.items(), key=lambda x:x[1], reverse=True)][:k]
        