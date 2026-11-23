class Solution:
    def sortArray(self, n: List[int]) -> List[int]:
        """
        consider a "divide and conquer" approach, where we recursive split the
        array in half, sort the smaller halves, then merge the two halves together.

        Once the smaller halves are sorted, to merge them together we set pointers at
        the beginning of each half and compare the elements at each of the pointers
        to see which is smaller. we add the smaller element to the merged list and
        increment that half's pointer.

        [10,9,1,1,1,2,3,1]

        [10,9,1,1] [1,2,3,1]

        [10, 9] [1, 1] [1, 2] [3, 1]

        [9, 10] [1, 1] [1, 2] [1, 3]

        [1, 1, 9, 10] [1, 1, 2, 3]

        [1,1,1,1,2,3,9,10]

        we'll need a helper function that splits an array in half and merges it back
        together in order in this way.
        """

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums


            first_half = mergeSort(nums[:len(nums)//2])
            second_half = mergeSort(nums[(len(nums)//2):])

            f_i, s_i = 0, 0
            new_array = []
            while f_i < len(first_half) or s_i < len(second_half):
                
                if f_i < len(first_half) and (s_i == len(second_half) or first_half[f_i] < second_half[s_i]):
                    new_array.append(first_half[f_i])
                    f_i += 1
                else:
                    new_array.append(second_half[s_i])
                    s_i += 1
            
            if f_i < len(first_half):
                new_array.extend(first_half[f_i:])
            if s_i < len(second_half):
                new_array.extend(second_half[s_i:])

            
            return new_array

        
        return mergeSort(n)




        
        