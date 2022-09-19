class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor : return 1  
        if (dividend == -2147483648 and divisor == -1): return 2147483647
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
        return answer if positive else -answer
