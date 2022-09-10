class Solution:
    def countPrimes(self, n: int) -> int:
        dp = [True for _ in range(n)];count = 0;
        if n <=1: return 0
        i = 2
        while(i*i<n):
            if dp[i]:
                for j in range(i*i,n,i):
                    dp[j] = False;
            i += 1
        return sum(dp)-2;
                
        