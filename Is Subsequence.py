class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        length=len(s)
        if length==0:
            return True
        for x in t:
            if s[i]==x:
                i+=1
            if length==i:
                return True
        return False



print(Solution.isSubsequence(Solution,"","ahbgdc"))

