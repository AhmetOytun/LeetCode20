from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(self, nums: List[int], x:int)->bool:
            l=0
            r=len(nums)-1
            while r>=l:
                mid=(l+r)//2
                if nums[mid]==x:
                    return True
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
    # optimize this part
        for num in matrix:
            if bs(Solution,num,target):
                return True
        return False

print(Solution.searchMatrix(Solution,[[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))