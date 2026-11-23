class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """

        """

        complements = dict()

        for i, num in enumerate(numbers):
            if target - num in complements:
                return [complements[target-num] + 1, i + 1]
            
            complements[num] = i
        