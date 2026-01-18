class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # Sort the array to easily access the smallest elements
        nums.sort()
        
        # Negate the smallest k elements
        for i in range(min(k, len(nums))):
            nums[i] = -nums[i]
        
        # If k is greater than the length of nums, we may need to negate again
        if k > len(nums):
            remaining_negations = k - len(nums)
            if remaining_negations % 2 == 1:
                # Negate the smallest element again if odd number of negations left
                nums[0] = -nums[0]
        
        # Return the x largest elements
        nums.sort(reverse=True)
        return nums[:x]