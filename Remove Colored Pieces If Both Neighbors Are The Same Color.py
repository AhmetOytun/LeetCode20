class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice=Solution.movefinder(Solution,colors.split('B'),'A')
        bob=Solution.movefinder(Solution,colors.split('A'),'B')
        if bob>=alice:
            return False
        else:
            return True

    def movefinder(self, lists: list,char: str) -> int:
        ret=0
        for x in lists:
            cnt=x.count(char)
            if cnt>2:
                ret+=cnt-2
        return ret

print(Solution.winnerOfGame(Solution,"ABBBBBBBAAA"))


