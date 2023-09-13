from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # solving by using two pointer method

        # assigning min max indexes to numbers
        num1=0
        num2=len(numbers)-1
        while True:
            # if sum is equal to target we just add 1 to indexes and return them
            if numbers[num1] + numbers[num2] == target:
                return [num1+1,num2+1]
            # if sum is greater than the target we decrease the right pointer by one
            elif numbers[num1] + numbers[num2] > target:
                num2-=1
            # if sum is smaller than the target we increase the left pointer by one
            else:
                num1+=1

print(Solution.twoSum(Solution,[2,7,11,15],9))
