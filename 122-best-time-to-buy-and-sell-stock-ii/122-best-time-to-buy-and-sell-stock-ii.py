class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0]*(2)for _ in range(N+1)]
        for index in range(N-1,-1,-1):
            for buy in range(0,2):
                if index == N:
                    dp[N][buy] = 1
                profit = 0
                if buy:
                    profit = max((-prices[index]+dp[index+1][0]),(dp[index+1][1]))
                else:
                    profit = max((prices[index]+dp[index+1][1]),(dp[index+1][0]))
                dp[index][buy] = profit
        return dp[0][1]
    
    
    # def solve(self,prices,index,buy,dp):
    #     if index == len(prices): return 0
    #     if dp[index][buy] != -1: return dp[index][buy]
    #     profit = 0
    #     if buy:
    #         profit = max((-prices[index]+self.solve(prices,index+1,0,dp)),(self.solve(prices,index+1,1,dp)))
    #     else:
    #         profit = max((prices[index]+self.solve(prices,index+1,1,dp)),(self.solve(prices,index+1,0,dp)))
    #     dp[index][buy] = profit
    #     return profit
        
        
        
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