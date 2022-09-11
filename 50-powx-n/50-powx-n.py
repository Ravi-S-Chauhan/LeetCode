class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n>=0: return self.solve2(x,n)
        else:
            return self.solve(x,n)
    def solve2(self,x,n):
        result = 1
        while n>0:
            if(n&1):
                result *= x
            x *= x
            n //= 2
        return result
    def solve(self,x,n):
        if n == 0: 
            return 1
        temp = self.solve(x,int(n/2))
        temp = temp*temp
        if n%2 == 0:
            return temp
        else:
            if n>0:
                return temp*x
            else:
                return temp/x