class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: 
            return 1
        temp = self.myPow(x,int(n/2))
        temp = temp*temp
        if n%2 == 0:
            return temp
        else:
            if n>0:
                return temp*x
            else:
                return temp/x