class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort();N = len(tokens)
        start = 0;end = N-1;score = 0
        if N == 0 or tokens[0]>power: return 0;
        while start<=end:
            if power>=tokens[start]:
                score += 1
                power -= tokens[start]
                start += 1
            elif score>0:
                power += tokens[end]
                score -= 1
                end -= 1
            else:
                break
        if start<N and power>=tokens[start]:score += 1
        return score
                
            
        