from typing import List

def generate(self, numRows: int) -> List[List[int]]:
    res = []
    for i in range(numRows):
        res.append(pascal(i))
    return res


def pascal(n):
    line = [1]
    for k in range(n):
        line.append((int)(line[k] * (n-k) / (k+1)))
    return line

print(pascal(0))