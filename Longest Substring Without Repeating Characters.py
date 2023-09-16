class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # solution using sliding window method
        rpt=set()
        l=0
        sol=0
        for r in range(len(s)):
            while s[r] in rpt:
                rpt.remove(s[l])
                l+=1
            rpt.add(s[r])
            sol=max(sol,r-l+1)
        return sol
print(Solution.lengthOfLongestSubstring(Solution,"abcabcbb"))