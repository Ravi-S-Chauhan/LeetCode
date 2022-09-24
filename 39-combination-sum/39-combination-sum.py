class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(temp,candidates,result,start,target):
            if target == 0:
                result.append(list(temp))
            while start<len(candidates) and candidates[start]<=target:
                temp.append(candidates[start])
                solve(temp,candidates,result,start,target-candidates[start])
                temp.pop()
                start+=1
        result = []
        solve([],sorted(candidates),result,0,target)
        return result
                