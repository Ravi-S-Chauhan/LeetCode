class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def solve(prices,dp,index,buy,k):
            N = len(prices)
            if index == N or k == 0: return 0
            if dp[index][buy][k] != -1:return dp[index][buy][k]
            if buy:
                profit = max((-prices[index]+solve(prices,dp,index+1,0,k)),(solve(prices,dp,index+1,1,k)))
            else:
                profit = max((prices[index]+solve(prices,dp,index+1,1,k-1)),(solve(prices,dp,index+1,0,k)))
            dp[index][buy][k] = profit
            return profit
        N = len(prices)
        if N <= 1 or k == 0: return 0
        dp = [[[-1]*(k+1) for _ in range(2)]for _ in range(N)]
        solve(prices,dp,0,1,k)
        print(dp)
        return dp[0][1][k]
        
            
        