class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if(abs(x-z) == abs(y-z)):
            return 0
        elif(abs(y-z) > abs(x-z)):
            return 1
        else:
            return 2
        