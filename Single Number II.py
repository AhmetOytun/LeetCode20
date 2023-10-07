from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nset = set()
        for x in nums:
            if x not in nset:
                nset.add(x)
                if nums.count(x) == 1:
                    return x
