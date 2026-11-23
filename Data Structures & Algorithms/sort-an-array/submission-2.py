class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
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
        aux = [0] * len(nums)
        
        def sort(lo, hi):
            if hi - lo <= 1:
                return
            
            mid = (hi + lo) // 2
            sort(lo, mid)
            sort(mid, hi)
            merge(lo, mid, hi)
        
        def merge(lo, mid, hi):
            i, j, k = lo, mid, 0
            
            while i < mid or j < hi:
                if i < mid and (j == hi or nums[i] < nums[j]):
                    aux[k] = nums[i]
                    i += 1
                    k += 1
                else:
                    aux[k] = nums[j]
                    j += 1
                    k += 1
            
            nums[lo:hi] = aux[:k]
        
        sort(0, len(nums))
        return nums






        