class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front = 0
        rear = len(heights) - 1
        max_area = 0
        while front < rear:
            width = rear - front
            height = min(heights[front], heights[rear])
            area = width * height
            max_area = max(max_area, area)
            if heights[front] < heights[rear]:
                front += 1
            else:
                rear -= 1
        return max_area
