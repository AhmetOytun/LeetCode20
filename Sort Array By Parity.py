from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for x in nums:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)
        return even + odd
print(Solution.sortArrayByParity(Solution,[3,1,2,4]))
