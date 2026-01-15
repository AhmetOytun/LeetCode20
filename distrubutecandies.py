from typing import List

def distributeCandies(candyType: List[int]) -> int:
    # get the max number of candies we can eat
    max_num = (len(candyType) // 2)

    # types array
    types = []

    # get all the different types
    for type in candyType:
        if type not in types:
            types.append(type)
        else:
            continue
    
    # unique types length
    unique = len(types)
    
    if max_num >= unique:
        return unique
    else:
        return max_num


    


print(distributeCandies([1,1,2,2,3,3]))
        