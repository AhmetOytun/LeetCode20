class Solution:
    def reverseWords(self, s: str) -> str:
        sol=""
        temp=""
        for w in s:
            if w==" ":
                sol+=temp[::-1]+" "
                temp=""
            else:
                temp+=w
        return sol
print(Solution.reverseWords(Solution,"Let's take LeetCode contest"))

