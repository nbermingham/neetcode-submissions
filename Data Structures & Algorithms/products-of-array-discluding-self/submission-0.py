class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        return an array whose elements are the product of all the elements besides the element at that index

        - numbers can be negative, positive, or zero

        idea: prefix and suffix products

        [1, 2, 4, 6]

        prefix: [1, 1, 2, 8]

        suffix: [48, 24, 6, 1]

        - calculate the prefix by starting on the left, keeping track of some current product, multiplying it
        by the most recent element in the original array and appending it to prefix array

        - suffix is calculated the same way but in reverse

        - multiply the prefix and the suffix array elements a given index to give the product array

        edge cases:
        - zeroes:


        - negative numbers:
        """

        prefixes, suffixes = [1], [1]

        curr_prod = 1
        for i in range(len(nums)-1):
            curr_prod *= nums[i]
            prefixes.append(curr_prod)

        curr_prod = 1
        for j in range(len(nums) - 1, 0, -1):
            curr_prod *= nums[j]
            suffixes.append(curr_prod)
        
        print(prefixes)
        print(suffixes[::-1])
        return [i*j for i, j in zip(prefixes, suffixes[::-1])]



        