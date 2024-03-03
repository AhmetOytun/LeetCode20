from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        sol = 0
        for x in nums:
            if x not in dic:
                dic[x] = nums.count(x)

        for y in dic.values():
            sol += (y * (y - 1)) // 2

        return sol

print(Solution.numIdenticalPairs(Solution,[1,2,3,1,1,3]))
