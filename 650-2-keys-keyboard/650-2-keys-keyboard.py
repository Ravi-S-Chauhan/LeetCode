class Solution:
    def minSteps(self, n: int) -> int:
        if n<=1: return 0
        i = 5;answer = 0;
        while n%2 == 0:
            n //=2
            answer += 2
        while n%3 == 0:
            n //=3
            answer += 3
        while i*i<=n:
            while(n%i == 0):
                answer += i
                n = n//i
            while (n%(i+2) == 0):
                answer += (i+2)
                n //=(i+2)
            i+= 6
        return answer if n<=3 else answer+n