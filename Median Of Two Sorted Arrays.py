from typing import List


class Solution:
    def findMedian(self,nums: List[int])->float:
        if len(nums)==0:
            return 0
        elif len(nums)%2==0:
            return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1])/2
        else:
            return float(nums[len(nums)//2])
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nl=nums1+nums2
        nl.sort()
        return Solution.findMedian(Solution,nl)
print(Solution.findMedianSortedArrays(Solution,[1,2],[3,4]))


