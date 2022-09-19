class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor : return 1  
        positive = (dividend>0 and divisor>0 or dividend<0 and divisor<0)
        a = abs(dividend)
        b = abs(divisor)
        answer = 0
        while a>=b:
            q = 0
            while a>(b<<(q+1)): 
                q+= 1
            answer += (1<<q)
            a -= (b<<q)
        # print(positive)
        ans =  answer if positive else -answer
        return min(max(ans,-2147483648),2147483647)