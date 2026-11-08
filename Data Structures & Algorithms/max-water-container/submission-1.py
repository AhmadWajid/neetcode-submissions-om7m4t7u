class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most = 0
        while left < right:
            width = right - left
            height = min(heights[right], heights[left])
            most = max(most, width * height)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return most
