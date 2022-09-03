class Solution {
public:
/*
    Keep track of the mx value of the difference between the maximum value and the current stock prices. Now if the difference between the mx value is > profit then we can update the profit
    return profit.
    
    mn = minimum stock price encountered
    profit = maximum profit that we can make.

*/
    int maxProfit(vector<int>& prices) {
        int mn = INT_MAX,profit = 0;
        for (int i = 0;i<prices.size();i++){
            if (prices[i]<mn) mn = prices[i];
            if (prices[i]-mn>profit) profit = prices[i]-mn;
        }
        return profit;
    }
};