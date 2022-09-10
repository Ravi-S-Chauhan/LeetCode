class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1]*(2)for _ in range(len(prices))]
        return self.solve(prices,0,1,dp)
    def solve(self,prices,index,buy,dp):
        if index == len(prices): return 0
        if dp[index][buy] != -1: return dp[index][buy]
        profit = 0
        if buy:
            profit = max((-prices[index]+self.solve(prices,index+1,0,dp)),(self.solve(prices,index+1,1,dp)))
        else:
            profit = max((prices[index]+self.solve(prices,index+1,1,dp)),(self.solve(prices,index+1,0,dp)))
        dp[index][buy] = profit
        return profit
        
        
        
        # N = len(prices)
        # if  start >= N-1: return 0
        # sell = -1
        # if start == -1 :
        #     start = 0
        # while start+1<N and prices[start+1]<prices[start]: 
        #     start += 1
        # end = start+1
        # while end+1 < N and prices[end]<prices[end+1]:
        #     end += 1
        # if start<N and end<N:
        #     return prices[end]-prices[start]+self.maxProfit(prices,end+1)
        # return 0