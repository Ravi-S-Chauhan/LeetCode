class Solution:
    def minSteps(self, n: int) -> int:
        if n<=1: return 0
        i = 2;answer = 0;
        while i*i<=n:
            while(n%i == 0):
                answer += i
                n = n//i
            i+= 1
        return answer if n<=1 else answer+n