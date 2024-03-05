class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        maxScore = 0
        i, j = 0, len(tokens) - 1
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                i += 1
                score += 1
                maxScore = max(maxScore, score)
            elif score > 0:
                power += tokens[j]
                j -= 1
                score -= 1
            else:
                break
        return maxScore