class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1 = nums.copy()
        # next index = (i + k) % len(nums)

        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = nums1[i]


        