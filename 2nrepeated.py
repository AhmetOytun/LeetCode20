from typing import List

def repeatedNTimes(nums: List[int]) -> int:
    added = []
    for num in nums:
        if num in added:
            return num
        else:
            added.append(num)


        