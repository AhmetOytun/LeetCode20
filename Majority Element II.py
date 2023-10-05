from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length=len(nums)/3
        dic={}
        sol=[]
        for x in nums:
            if x not in dic:
                dic[x]=nums.count(x)
            else:
                continue
        for y in dic.keys():
            if dic[y]>length:
                sol.append(y)
        return sol

