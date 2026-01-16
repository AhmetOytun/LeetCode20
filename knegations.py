from typing import List

def largestSumAfterKNegations(nums: List[int], k: int) -> int:
    # result variable
    res = 0

    # sort the numbers at first 
    nums.sort()

    # first change the negative numbers into positive ones while k > 0
    for x in range(len(nums)):
        if nums[x] < 0 and k > 0:
            nums[x] = abs(nums[x])
            res += nums[x]
            k -= 1
        else:
            res += nums[x]
            continue
    print(res)
    
    # sort again
    nums.sort()
    
    # then if k is still bigger than 0 modify the smallest num if k % 2 = 1
    if k % 2 == 1:
        nums[0] = nums[0] * -1
        res += nums[0] * 2
    
    return res
    




print(largestSumAfterKNegations([4,2,3],1))
        