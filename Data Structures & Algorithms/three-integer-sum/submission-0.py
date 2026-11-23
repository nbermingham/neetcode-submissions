class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]

            d = set()

            for j in range(i+1, len(nums)):
                if target - nums[j] in d:
                    new = (nums[i], target - nums[j], nums[j])
                    res.add(new)
                d.add(nums[j])
            
        return [list(t) for t in res]