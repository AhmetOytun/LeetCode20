from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if len(nums)<2:
            return True
        inc=-1
        for x in range(1,len(nums)):
            if nums[x]>nums[x-1]:
                if inc==-1:
                    inc=0
                elif inc==1:
                    return False
            elif nums[x]<nums[x-1]:
                if inc==-1:
                    inc=1
                elif inc==0:
                    return False
        return True



print(Solution.isMonotonic(Solution,[1,0,-1]))