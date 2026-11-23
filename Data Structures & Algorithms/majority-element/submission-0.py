class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = dict()
        threshold = (len(nums) // 2) + 1
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

            if counter[num] == threshold:
                return num
        