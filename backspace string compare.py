class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if Solution.solfunc(Solution,s)==Solution.solfunc(Solution,t):
            return True
        return False

    def solfunc(self, s: str) -> str:
        sol=""
        stack=[]

        for x in s:
            if x=='#' and stack:
                stack.pop()
            elif x!='#':
                stack.append(x)
            else:
                continue

        for x in stack:
            sol+=x

        return sol

Solution.backspaceCompare(Solution,"123","123")

