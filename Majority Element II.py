from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length=len(nums)/3
        nset=set()
        sol=[]
        for x in nums:
            if x not in nset:
                nset.add(x)
                if nums.count(x)>length:
                    sol.append(x)
        return sol
print(Solution.majorityElement(Solution,[3,2,3]))

