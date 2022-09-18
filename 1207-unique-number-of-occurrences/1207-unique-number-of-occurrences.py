class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        for k,v in Counter(arr).items():
            if v in seen:
                return False
            seen.add(v)
        return True