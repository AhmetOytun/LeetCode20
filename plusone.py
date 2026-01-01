from typing import List

def plusOne(digits: List[int]) -> List[int]:
    number = 0
    power = len(digits) - 1
    
    for digit in digits:
        number += digit * pow(10, power)
        power -= 1

    return [int(d) for d in str(number + 1)]


        