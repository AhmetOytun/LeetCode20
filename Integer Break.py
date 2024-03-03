class Solution:
    def integerBreak(self, n: int) -> int:
        if n<4:
            return n-1
        elif n%3==0:
            return 3**(n//3)
        elif n%3==1:
            return 3**(n // 3 -1)*4
        elif n%3==2:
            return 3**(n // 3 )*2
print(Solution.integerBreak(Solution,10))

