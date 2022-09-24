class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(temp,can,target,start,result):
            if target == 0:
                result.append(list(temp))
            prev = 0
            while start<len(can) and can[start]<=target:
                if prev!=can[start]:
                    temp.append(can[start])
                    solve(temp,can,target-can[start],start+1,result)
                    temp.pop()
                    prev = can[start]
                start+= 1
        result = []
        can = sorted(candidates)
        solve([],can,target,0,result)
        return result
        