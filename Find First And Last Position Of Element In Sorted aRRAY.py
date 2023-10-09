from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        else:
            return [nums.index(target), len(nums) - 1 - nums[::-1].index(target)]
print(Solution.searchRange(Solution,[5,7,7,8,8,10],8))

