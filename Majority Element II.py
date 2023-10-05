from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length=len(nums)/3
        dic={}
        sol=[]
        for x in nums:
            if x not in dic:
                dic[x]=nums.count(x)
                if dic[x]>length:
                    sol.append(x)
            else:
                continue
        return sol
print(Solution.majorityElement(Solution,[3,2,3]))

