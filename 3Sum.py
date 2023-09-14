from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # solution using two pointers technique and sets
        sol=set()
        nums.sort()
        length=len(nums)
        for i in range(length):
            j=i+1
            k=length-1
            while k>j:
                sum=nums[i]+nums[k]+nums[j]
                if sum==0:
                    sol.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif sum>0:
                    k-=1
                else:
                    j+=1
        return list(sol)

print(Solution.threeSum(Solution,[-1,0,1,2,-1,-4]))




