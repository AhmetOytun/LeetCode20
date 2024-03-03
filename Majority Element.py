from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length=len(nums)/2
        for x in set(nums):
            if nums.count(x)>length:
                return x
print(Solution.majorityElement(Solution,[3,2,3]))
