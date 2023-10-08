from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        hmap = {0:0,1:0,2:0}
        ct=0
        for x in hmap.keys():
            hmap[x]=nums.count(x)
        for x in hmap.keys():
            while hmap[x]!=0:
                nums[ct]=x
                ct+=1
                hmap[x]-=1
        return nums

print(Solution.sortColors(Solution,[2,0,2,1,1,0]))

