import collections
from typing import List

"""
class Solution:
    # brute force solution(has time complexity issues)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window=[]
        sol=[]

        for x in range(k):
            window.append(nums[x])

        sol.append(max(window))

        for x in range(k,len(nums)):
            window.pop(0)
            window.append(nums[x])
            sol.append(max(window))

        return sol

print(Solution.maxSlidingWindow(Solution,[1,3,-1,-3,5,3,6,7],3))
"""

# deque solution

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq=collections.deque()
        sol=[]
        l=r=0

        while r < len(nums):
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)


            if l>deq[0]:
                deq.popleft()

            if (r+1)>=k:
                sol.append(nums[deq[0]])
                l+=1
            r+=1

        return sol

print(Solution.maxSlidingWindow(Solution,[1,3,-1,-3,5,3,6,7],3))









