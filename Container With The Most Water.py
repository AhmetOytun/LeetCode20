from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # solution using two pointer method
        maxArea=0
        left=0
        right=len(height)-1
        while left<right:
            curArea=min(height[left], height[right]) * (right - left)
            if curArea>maxArea:
                maxArea=curArea
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return maxArea

print(Solution.maxArea(Solution,[1,8,6,2,5,4,8,3,7]))