class Solution:
    def countPrimes(self, n: int) -> int:
        dp = [True for _ in range(n)];count = 0;
        i = 2
        while(i*i<n):
            if dp[i]:
                for j in range(i*i,n,i):
                    dp[j] = False;
            i += 1
        for i in range(2,n):
            if dp[i]:
                count += 1;
        return count;
                
        