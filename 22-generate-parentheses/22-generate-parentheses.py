class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(temp,op,cp,result):
            if op == 0 and cp == 0:
                result.append(temp)
                return
            if op:
                solve(temp+'(',op-1,cp,result)
            if op<cp and cp:
                solve(temp+')',op,cp-1,result)
        result = []
        solve("",n,n,result)
        return result