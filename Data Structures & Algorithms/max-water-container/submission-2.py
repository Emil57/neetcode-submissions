class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx = 0
        l, r = 0, len(heights)-1

        while l < r: 
            b = (r-l)
            h = min(heights[l], heights[r])
            area = b * h
            maxx = max(maxx, area)
            if heights[l] < heights[r]: l+=1
            else: r -=1 
        return maxx
