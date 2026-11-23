class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i, h1 in enumerate(heights):
            for j, h2 in enumerate(heights):
                max_area = max(max_area, (j - i) * min(h1, h2))

        return max_area