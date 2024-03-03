from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        mid=0

        while low<=high:
            mid = (high+low)//2

            if nums[mid]>x:
                high=mid-1
            elif nums[mid]<x:
                low=mid+1
            else:
                return mid
        return -1