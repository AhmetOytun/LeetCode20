from typing import List
from math import sqrt

def sumFourDivisors(nums: List[int]) -> int:
    total_sum = 0
    
    for num in nums:
        divisors = set()
        # Only iterate up to the square root
        for x in range(1, int(sqrt(num)) + 1):
            if num % x == 0:
                divisors.add(x)
                divisors.add(num // x)
            
            # Optimization: if we already exceeded 4, stop looking
            if len(divisors) > 4:
                break
        
        # If the number has exactly 4 divisors, add their sum to our total
        if len(divisors) == 4:
            total_sum += sum(divisors)
            
    return total_sum

# Correct way to call it with a list
print(sumFourDivisors([21, 4, 7])) 
# 21 has divisors (1, 3, 7, 21) -> sum is 32. 
# 4 and 7 do not have exactly 4 divisors.