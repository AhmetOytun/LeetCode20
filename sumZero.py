from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        # result array
        res = []

        for x in range(1,(n//2) + 1):
            # append the number positive then negative
            res.append(x)
            res.append(-x)

        if n % 2 == 1:
            res.append(0)

        return res
        