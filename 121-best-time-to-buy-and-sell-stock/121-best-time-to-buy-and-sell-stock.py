class Solution:
    """
    Keep track of the mx value of the difference between the maximum value and the current stock prices. Now if the difference between the mx value is > profit then we can update the profit
    return profit.
    
    mn = minimum stock price encountered
    profit = maximum profit that we can make.

    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0;mn = sys.maxsize;
        for i in prices:
            if i<mn :
                mn = i
            newProfit = i - mn;
            if newProfit > profit:
                profit = newProfit;
        return profit;