from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0
        
        nums.sort()
        min_removals = n  # Start with the worst case: remove all elements

        left = 0
        for right in range(n):
            while nums[right] - nums[left] > 1:
                left += 1
            current_removals = n - (right - left + 1)
            min_removals = min(min_removals, current_removals)

        return min_removals
        