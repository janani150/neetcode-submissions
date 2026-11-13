class Solution:
    def maxArea(self, heights: List[int]) -> int:
        count_max=0
        n=len(heights)
        left=0
        right=n-1

        while left<=right:
            width=right-left
            height=min(heights[left],heights[right])
            area=width*height
            count_max=max(area,count_max)

            if heights[left]<heights[right]:
                left=left+1
            else:
                right=right-1
        return count_max