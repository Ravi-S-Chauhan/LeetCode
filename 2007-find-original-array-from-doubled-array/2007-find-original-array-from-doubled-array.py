class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        N = len(changed);result = []
        if N & 1: return []
        count = Counter(changed);changed.sort();
        for num in changed:
            if num == 0 and count[num]>=2:
                count[num] -= 2
                result.append(num)
            elif num>0 and count[num] and count[2*num]:
                count[num] -= 1;count[2*num] -= 1;
                result.append(num)
        return result if len(result) == N//2 else []