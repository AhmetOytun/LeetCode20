from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))

print(intersection([1,2,2,1],[2,2]))