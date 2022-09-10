class Solution:
    def maxProfit(self, prices: List[int],start = -1) -> int:
        N = len(prices)
        if  start >= N-1: return 0
        sell = -1
        if start == -1 :
            start = 0
        while start+1<N and prices[start+1]<prices[start]: 
            start += 1
        end = start+1
        while end+1 < N and prices[end]<prices[end+1]:
            end += 1
        if start<N and end<N:
            return prices[end]-prices[start]+self.maxProfit(prices,end+1)
        return 0