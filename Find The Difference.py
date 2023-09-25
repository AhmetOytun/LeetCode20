class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        aset=set()
        for x in t:
            if t in aset:
                continue
            else:
                if s.count(x)!=t.count(x):
                    return x
                else:
                    aset.add(x)
    # greatly optimized



print(Solution.findTheDifference(Solution,"abcd","abcde"))
