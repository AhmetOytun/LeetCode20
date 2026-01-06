from typing import List

def findRelativeRanks(score: List[int]) -> List[str]:
    sorted_score = score.copy()
    sorted_score.sort(reverse=True)
    sorted_index = {v: i for i, v in enumerate(sorted_score)}
    result = []
    for s in score:
        rank = sorted_index[s]
        if rank == 0:
            result.append("Gold Medal")
        elif rank == 1:
            result.append("Silver Medal")
        elif rank == 2:
            result.append("Bronze Medal")
        else:
            result.append(str(rank + 1))
    return result

findRelativeRanks([5,4,3,2,1])
        