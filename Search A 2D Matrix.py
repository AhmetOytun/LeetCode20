from typing import List
# needs optimization for len=1 arrays

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1=l2=m1=m2=0
        r1,r2=len(matrix)-1,len(matrix[0])-1
        while r1>=l1:
            m1=(r1+l1)//2
            print(f"m1={m1}")
            print(len(matrix))
            if matrix[m1][0] <= target <= matrix[m1][len(matrix[0]) - 1]:
                while r2 >= l2:
                    print(f"m2={m2}")
                    m2 = (r2 + l2) // 2
                    if matrix[m1][m2]>target:
                        r2=m2-1
                    elif matrix[m1][m2]<target:
                        l2=m2+1
                    else:
                        return True
                return False
            elif matrix[m1][0]>target:
                r1=m1-1
            elif matrix[m1][0]<target:
                l1=m1-1
            else:
                return False
        return False
print(Solution.searchMatrix(Solution,[[1,3,5,7],[10,11,16,20],[23,30,34,60]],11))





