class Solution:
    # OPTIMIZE THIS PLS THIS LOOKS SO CRINGE
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0


        while high>=low:
            mid = (high + low) // 2
            if nums[low]<=nums[high]:
                return nums[low]

            elif nums[mid] >= nums[low]:
                low = mid + 1

            else:
                high = mid - 1
        return nums[mid]