class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1

        max_amount = (end - start) * min(heights[start], heights[end])
        while start < end:
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
            max_amount = max((end - start) * min(heights[start], heights[end]), max_amount)
        return max_amount